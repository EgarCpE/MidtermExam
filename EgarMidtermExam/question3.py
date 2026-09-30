import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit 


def displayName():
    name = inputName.text()
    outputName.setText(name)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Midterm in OOP")
window.setGeometry(400, 500, 750, 400)

label = QLabel("Enter your fullname", window)
label.setGeometry(100, 120, 200, 30)

inputName = QLineEdit(window)
inputName.setGeometry(400, 115, 300, 40)

button = QPushButton("Click to display your fullname", window)
button.setGeometry(100, 180, 250, 40)

outputName = QLabel("", window)
outputName.setGeometry(400, 180, 300, 40)

button.clicked.connect(displayName)

window.show()
sys.exit(app.exec())