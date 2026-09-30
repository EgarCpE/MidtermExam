import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


def change_color():
	button.setStyleSheet("background-color: yellow;")


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Special Midterm Exam in OOP2")
window.setGeometry(400, 200, 500, 400)

button = QPushButton("Click to Change the Color", window)
button.setGeometry(160, 180, 180, 40)

button.clicked.connect(change_color)

window.show()

sys.exit(app.exec())