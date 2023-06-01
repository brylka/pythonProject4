import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QTextEdit, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabliczka mnożenia")
        self.setGeometry(100, 100, 500, 500)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createMultiplicationTable()
        self._createOutputArea()

    def _createMultiplicationTable(self):
        buttonsLayout = QGridLayout()
        self.buttonMap = {}

        for i in range(1, 11):
            for j in range(1, 11):
                result = i * j
                button = QPushButton(str(result))
                button.clicked.connect(self._showMultiplication)
                buttonsLayout.addWidget(button, i - 1, j - 1)
                self.buttonMap[str(result)] = (i, j)

        self.generalLayout.addLayout(buttonsLayout)

    def _createOutputArea(self):
        self.outputArea = QTextEdit()
        self.outputArea.setReadOnly(True)
        self.generalLayout.addWidget(self.outputArea)

    def _showMultiplication(self):
        button_text = self.sender().text()
        i, j = self.buttonMap[button_text]
        self.outputArea.setText(f"{i} * {j} = {button_text}")

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()