# Nama : Valerine Jesika Dewi
# NIM : F1D02310027  
# Kelas : Visual Programming C

# Tugas 3 - Form Login

import sys
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QCheckBox, QFrame)
from PySide6.QtCore import Qt

class FormLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Login")
        self.resize(400, 420)
        self.setStyleSheet("background-color: #f5f5f5;")

        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(30, 30, 30, 30)

        # Header
        judul = QLabel("LOGIN")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            padding: 14px;
            background-color: #7B2FBE;
            color: white;
            border-radius: 8px;
        """)

        # Username
        label_username = QLabel("Username:")
        label_username.setStyleSheet("font-size: 13px; background-color: transparent;")

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Masukkan username...")
        self.input_username.setStyleSheet("""
            font-size: 14px;
            padding: 10px;
            background-color: white;
            border-radius: 6px;
            border: 2px solid #ccc;
        """)

        # Password
        label_password = QLabel("Password:")
        label_password.setStyleSheet("font-size: 13px; background-color: transparent;")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Masukkan password...")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setStyleSheet("""
            font-size: 14px;
            padding: 10px;
            background-color: white;
            border-radius: 6px;
            border: 2px solid #ccc;
        """)

        # Checkbox tampilkan password
        self.checkbox_show = QCheckBox("Tampilkan Password")
        self.checkbox_show.setStyleSheet("font-size: 13px; background-color: transparent;")
        self.checkbox_show.stateChanged.connect(self.toggle_password)

        # Tombol Login & Reset
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        btn_login = QPushButton("Login")
        btn_login.setStyleSheet("""
            QPushButton {
                font-size: 13px;
                font-weight: bold;
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover { background-color: #388E3C; }
            QPushButton:pressed { background-color: #1B5E20; }
        """)
        btn_login.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_login.clicked.connect(self.proses_login)

        btn_reset = QPushButton("Reset")
        btn_reset.setStyleSheet("""
            QPushButton {
                font-size: 13px;
                font-weight: bold;
                padding: 10px;
                background-color: #9E9E9E;
                color: white;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover { background-color: #757575; }
            QPushButton:pressed { background-color: #424242; }
        """)
        btn_reset.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_reset.clicked.connect(self.reset_form)

        btn_layout.addWidget(btn_login)
        btn_layout.addWidget(btn_reset)

        # Frame pesan hasil
        self.frame_pesan = QFrame()
        self.frame_pesan.setVisible(False)
        self.frame_pesan.setStyleSheet("""
            QFrame {
                border-radius: 6px;
                border-left: 5px solid #4CAF50;
                background-color: #E8F5E9;
            }
        """)

        pesan_layout = QVBoxLayout()
        pesan_layout.setContentsMargins(12, 10, 12, 10)

        self.label_pesan = QLabel("")
        self.label_pesan.setStyleSheet("font-size: 13px; background-color: transparent; border: none;")
        self.label_pesan.setWordWrap(True)

        pesan_layout.addWidget(self.label_pesan)
        self.frame_pesan.setLayout(pesan_layout)

        # Susun layout utama
        layout.addWidget(judul)
        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.checkbox_show)
        layout.addLayout(btn_layout)
        layout.addWidget(self.frame_pesan)
        layout.addStretch()

        self.setLayout(layout)

    def toggle_password(self, state):
        if state == Qt.CheckState.Checked.value:
            self.input_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

    def proses_login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        # Validasi login
        if username == "admin" and password == "12345":
            # Login berhasil - tampilan hijau
            self.frame_pesan.setStyleSheet("""
                QFrame {
                    border-radius: 6px;
                    border-left: 5px solid #4CAF50;
                    background-color: #E8F5E9;
                }
            """)
            self.label_pesan.setStyleSheet("font-size: 13px; color: #2E7D32; background-color: transparent; border: none;")
            self.label_pesan.setText(f"Login berhasil! Selamat datang, {username}.")

            # Highlight input hijau
            self.input_username.setStyleSheet("""
                font-size: 14px; padding: 10px;
                background-color: #E8F5E9;
                border-radius: 6px; border: 2px solid #4CAF50;
            """)
            self.input_password.setStyleSheet("""
                font-size: 14px; padding: 10px;
                background-color: #E8F5E9;
                border-radius: 6px; border: 2px solid #4CAF50;
            """)
        else:
            # Login gagal - tampilan merah
            self.frame_pesan.setStyleSheet("""
                QFrame {
                    border-radius: 6px;
                    border-left: 5px solid #F44336;
                    background-color: #FFEBEE;
                }
            """)
            self.label_pesan.setStyleSheet("font-size: 13px; color: #C62828; background-color: transparent; border: none;")
            self.label_pesan.setText("Login gagal! Username atau password salah.")

            # Highlight input merah
            self.input_username.setStyleSheet("""
                font-size: 14px; padding: 10px;
                background-color: #FFEBEE;
                border-radius: 6px; border: 2px solid #F44336;
            """)
            self.input_password.setStyleSheet("""
                font-size: 14px; padding: 10px;
                background-color: #FFEBEE;
                border-radius: 6px; border: 2px solid #F44336;
            """)

        self.frame_pesan.setVisible(True)

    def reset_form(self):
        self.input_username.clear()
        self.input_password.clear()
        self.checkbox_show.setChecked(False)
        self.frame_pesan.setVisible(False)

        # Reset style input
        style_default = """
            font-size: 14px; padding: 10px;
            background-color: white;
            border-radius: 6px; border: 2px solid #ccc;
        """
        self.input_username.setStyleSheet(style_default)
        self.input_password.setStyleSheet(style_default)


app = QApplication(sys.argv)
window = FormLogin()
window.show()
sys.exit(app.exec())