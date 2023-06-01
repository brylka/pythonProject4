import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class MultiplicationButton(QPushButton):
    def __init__(self, text, i, j, outputLabel):
        super().__init__(text)
        self.i = i
        self.j = j
        self.outputLabel = outputLabel

    def enterEvent(self, event):
        self.outputLabel.setText(f"{self.i} * {self.j} = {self.text()}")

    def leaveEvent(self, event):
        self.outputLabel.clear()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabliczka mnożenia")
        self.setGeometry(100, 100, 500, 500)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createOutputLabel()
        self._createMultiplicationTable()

    def _createMultiplicationTable(self):
        buttonsLayout = QGridLayout()

        for i in range(1, 12):
            for j in range(1, 12):
                if i == 1 and j == 1:
                    label = QLabel("*")
                elif i == 1:
                    label = QLabel(str(j - 1))
                elif j == 1:
                    label = QLabel(str(i - 1))
                else:
                    result = (i - 1) * (j - 1)
                    button = MultiplicationButton(str(result), i - 1, j - 1, self.outputLabel)
                    buttonsLayout.addWidget(button, i - 1, j - 1)
                    continue
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                buttonsLayout.addWidget(label, i - 1, j - 1)

        self.generalLayout.addLayout(buttonsLayout)

    def _createOutputLabel(self):
        self.outputLabel = QLabel()
        self.outputLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(50)
        self.outputLabel.setFont(font)
        self.generalLayout.addWidget(self.outputLabel)

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()