import cv2
import numpy as np
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap

class VideoTrackingWorker(QObject):
    frame_ready = pyqtSignal(QPixmap)
    telemetry_ready = pyqtSignal(float, float, bool)

    def __init__(self, stream_url="udp://127.0.0.1:5000"):
        super().__init__()
        self.stream_url = stream_url
        self.running = True
        self.pan_degree = 0.0
        self.tilt_degree = 0.0

    def process_stream(self):
        cap = cv2.VideoCapture(self.stream_url, cv2.CAP_FFMPEG)
        tracker = cv2.TrackerKCF_create()
        tracking_locked = False
        bbox = (100, 100, 80, 80)

        while self.running:
            ret, frame = cap.read()
            if not ret:
                continue

            h, w, _ = frame.shape
            cx, cy = w // 2, h // 2

            if not tracking_locked:
                tracker.init(frame, bbox)
                tracking_locked = True

            success, box = tracker.update(frame)
            if success:
                bx, by, bw, bh = [int(v) for v in box]
                tx, ty = bx + (bw // 2), by + (bh // 2)
                
                cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (0, 255, 204), 2)
                cv2.line(frame, (cx, cy), (tx, ty), (0, 255, 204), 1)
                
                error_x = tx - cx
                error_y = ty - cy
                
                self.pan_degree = (error_x / cx) * 45.0
                self.tilt_degree = -(error_y / cy) * 30.0

            self.telemetry_ready.emit(self.pan_degree, self.tilt_degree, success)

            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            qt_img = QImage(rgb_image.data, w, h, w * 3, QImage.Format.Format_RGB888)
            self.frame_ready.emit(QPixmap.fromImage(qt_img))

        cap.release()

    def stop(self):
        self.running = False