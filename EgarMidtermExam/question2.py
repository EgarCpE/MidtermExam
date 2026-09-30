import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

# Changing the color button to yellow
def change_color():
	button.setStyleSheet("background-color: yellow;")


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Special Midterm Exam in OOP2")
window.setGeometry(400, 200, 500, 400)

#creating the button 
button = QPushButton("Click to Change the Color", window)
button.setGeometry(160, 180, 180, 40)

#function needed for the button to work
button.clicked.connect(change_color)

window.show()

sys.exit(app.exec())
