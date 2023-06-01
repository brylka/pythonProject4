import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signals and slots")

        self.layout = QVBoxLayout()

        self.button = QPushButton("Greet")
        self.button.clicked.connect(self.greet)

        self.layout.addWidget(self.button)

        self.msgLabel = QLabel("")
        self.layout.addWidget(self.msgLabel)

        self.setLayout(self.layout)

    def greet(self):
        if self.msgLabel.text():
            self.msgLabel.setText("")
        else:
            self.msgLabel.setText("Hello, World!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()