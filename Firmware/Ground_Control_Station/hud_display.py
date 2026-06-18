from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class TacticalHUDWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        self.title_lbl = QLabel("[ SYSTEM TELEMETRY ]")
        self.title_lbl.setStyleSheet("font-family: 'Space Mono'; font-weight: bold; font-size: 14px; color: #00FFCC;")
        self.title_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_lbl)

        self.yaw_lbl = QLabel("YAW DEGREE: 0.00°")
        self.pitch_lbl = QLabel("PITCH DEGREE: 0.00°")
        self.status_lbl = QLabel("STATUS: SEARCHING")

        style = "font-family: 'Space Mono'; font-size: 12px; color: #A0C0D0; padding: 5px;"
        for lbl in [self.yaw_lbl, self.pitch_lbl, self.status_lbl]:
            lbl.setStyleSheet(style)
            layout.addWidget(lbl)
            
        layout.addStretch()

    def update_telemetry(self, yaw, pitch, locked):
        self.yaw_lbl.setText(f"YAW DEGREE: {yaw:+.2f}°")
        self.pitch_lbl.setText(f"PITCH DEGREE: {pitch:+.2f}°")
        if locked:
            self.status_lbl.setText("STATUS: TARGET_LOCKED")
            self.status_lbl.setStyleSheet("font-family: 'Space Mono'; font-size: 12px; color: #00FFCC; font-weight: bold;")
        else:
            self.status_lbl.setText("STATUS: LOST_TRACK")
            self.status_lbl.setStyleSheet("font-family: 'Space Mono'; font-size: 12px; color: #FF3366; font-weight: bold;")