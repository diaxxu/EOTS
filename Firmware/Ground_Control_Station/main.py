import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from hud_display.py import TacticalHUDWidget
from tracking.py import VideoTrackingWorker

class GroundControlStation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PROJECT EOTS - GROUND CONTROL STATION")
        self.resize(1280, 720)
        self.setStyleSheet("background-color: #0A0F14; color: #00FFCC;")

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        self.feed_container = QWidget()
        feed_layout = QVBoxLayout(self.feed_container)
        self.video_frame = QLabel("AWAITING FEED...")
        self.video_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_frame.setStyleSheet("border: 2px solid #121B2A; background-color: #020508;")
        feed_layout.addWidget(self.video_frame)
        main_layout.addWidget(self.feed_container, stretch=3)

        self.sidebar = QWidget()
        self.sidebar.setStyleSheet("background-color: #060A0F; border-left: 2px solid #121B2A;")
        sidebar_layout = QVBoxLayout(self.sidebar)
        
        self.hud_telemetry = TacticalHUDWidget()
        sidebar_layout.addWidget(self.hud_telemetry)
        main_layout.addWidget(self.sidebar, stretch=1)

        self.tracking_thread = QThread()
        self.worker = VideoTrackingWorker("udp://127.0.0.1:5000")
        self.worker.moveToThread(self.tracking_thread)
        
        self.tracking_thread.started.connect(self.worker.process_stream)
        self.worker.frame_ready.connect(self.update_screen)
        self.worker.telemetry_ready.connect(self.hud_telemetry.update_telemetry)
        
        self.tracking_thread.start()

    def update_screen(self, qt_image):
        self.video_frame.setPixmap(qt_image)

    def closeEvent(self, event):
        self.worker.stop()
        self.tracking_thread.quit()
        self.tracking_thread.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GroundControlStation()
    window.show()
    sys.exit(app.exec())