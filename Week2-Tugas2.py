# Nama : Valerine Jesika Dewi
# NIM : F1D02310027  
# Kelas : Visual Programming C

# Tugas 2 - Konversi Suhu

import sys
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QFrame)
from PySide6.QtCore import Qt

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.resize(400, 400)
        self.setStyleSheet("background-color: #f0f4f8;")

        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)

        judul = QLabel("KONVERSI SUHU")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet("""
            font-size: 22px; 
            font-weight: bold; 
            padding: 14px; 
            background-color: #2196F3; 
            color: white; 
            border-radius: 5px;
        """)

        label_input = QLabel("Masukkan Suhu (Celsius):")
        label_input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_input.setStyleSheet("font-size: 13px; padding: 2px; background-color: transparent;")

        self.input_suhu = QLineEdit()
        self.input_suhu.setPlaceholderText("Masukkan angka...")
        self.input_suhu.setStyleSheet("""
            font-size: 15px; 
            padding: 10px; 
            background-color: #E8F5E9; 
            border-radius: 6px; 
            border: 2px solid #81C784;
        """)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        for label in ["Fahrenheit", "Kelvin", "Reamur"]:
            btn = QPushButton(label)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 13px;
                    font-weight: bold;
                    padding: 10px;
                    background-color: #2196F3;
                    color: white;
                    border-radius: 6px;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #1976D2;
                }
                QPushButton:pressed {
                    background-color: #0D47A1;
                }
            """)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, l=label: self.konversi(l))
            btn_layout.addWidget(btn)

        self.frame_hasil = QFrame()
        self.frame_hasil.setStyleSheet("""
            QFrame {
                background-color: #BBDEFB;
                border-radius: 8px;
                border-left: 4px solid #23395d;
            }
        """)
        self.frame_hasil.setVisible(False)

        hasil_layout = QVBoxLayout()
        hasil_layout.setContentsMargins(12, 10, 12, 10)

        label_judul_hasil = QLabel("Hasil Konversi:")
        label_judul_hasil.setStyleSheet("font-size: 13px; font-weight: bold; background-color: transparent; border: none; color : #23395d")


        self.label_hasil = QLabel("")
        self.label_hasil.setStyleSheet("font-size: 14px; background-color: transparent; border: none; color : #23395d")

        hasil_layout.addWidget(label_judul_hasil)
        hasil_layout.addWidget(self.label_hasil)
        self.frame_hasil.setLayout(hasil_layout)

        layout.addWidget(judul)
        layout.addWidget(label_input)
        layout.addWidget(self.input_suhu)
        layout.addSpacing(10)
        layout.addLayout(btn_layout)
        layout.addWidget(self.frame_hasil, 1)
        layout.addStretch()

        self.setLayout(layout)

    def konversi(self, jenis):
        input_text = self.input_suhu.text()

        try:
            celsius = float(input_text)
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Input harus berupa angka!")
            return

        if jenis == "Fahrenheit":
            hasil = (celsius * 9 / 5) + 32
        elif jenis == "Kelvin":
            hasil = celsius + 273.15
        elif jenis == "Reamur":
            hasil = celsius * 4 / 5

        self.label_hasil.setText(f"{celsius} Celsius = {hasil:.2f} {jenis}")
        self.frame_hasil.setVisible(True)

app = QApplication(sys.argv)
window = KonversiSuhu()
window.show()
sys.exit(app.exec())