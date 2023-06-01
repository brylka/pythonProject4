import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class MultiplicationButton(QPushButton):
    def __init__(self, text, i, j, mainWindow):
        super().__init__(text)
        self.i = i
        self.j = j
        self.mainWindow = mainWindow

    def enterEvent(self, event):
        self.mainWindow.outputLabel.setText(f"{self.i} * {self.j} = {self.text()}")
        for button in self.mainWindow.rowButtonMap[self.i][:self.j]:
            button.setStyleSheet("background-color: lightblue")
        for button in self.mainWindow.colButtonMap[self.j][:self.i]:
            button.setStyleSheet("background-color: lightblue")
        self.mainWindow.rowLabels[self.i].setStyleSheet("background-color: lightblue")
        self.mainWindow.colLabels[self.j].setStyleSheet("background-color: lightblue")

    def leaveEvent(self, event):
        self.mainWindow.outputLabel.clear()
        for button in self.mainWindow.rowButtonMap[self.i][:self.j]:
            button.setStyleSheet("")
        for button in self.mainWindow.colButtonMap[self.j][:self.i]:
            button.setStyleSheet("")
        self.mainWindow.rowLabels[self.i].setStyleSheet("")
        self.mainWindow.colLabels[self.j].setStyleSheet("")

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
        self.buttonSize = 30
        self.labelSize = 30
        self.rowButtonMap = {i: [] for i in range(11)}
        self.colButtonMap = {j: [] for j in range(11)}
        self.rowLabels = {i: None for i in range(11)}
        self.colLabels = {j: None for j in range(11)}

        for i in range(1, 12):
            for j in range(1, 12):
                if i == 1 and j == 1:
                    label = QLabel("*")
                    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    label.setFixedSize(self.labelSize, self.labelSize)
                    buttonsLayout.addWidget(label, i - 1, j - 1)
                elif i == 1 or j == 1:
                    label = QLabel(str(max(i - 1, j -1 )))
                    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    label.setFixedSize(self.labelSize, self.labelSize)
                    buttonsLayout.addWidget(label, i - 1, j - 1)
                    if i == 1:
                        self.colLabels[j - 1] = label
                    if j == 1:
                        self.rowLabels[i - 1] = label
                else:
                    result = (i-1) * (j-1)
                    button = MultiplicationButton(str(result), i - 1, j - 1, self)
                    button.setFixedSize(self.buttonSize, self.buttonSize)
                    self.rowButtonMap[i - 1].append(button)
                    self.colButtonMap[j - 1].append(button)
                    buttonsLayout.addWidget(button, i - 1, j - 1)

        self.generalLayout.addLayout(buttonsLayout)

    def _createOutputLabel(self):
        self.outputLabel = QLabel()
        self.outputLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(40)
        self.outputLabel.setFont(font)
        self.generalLayout.addWidget(self.outputLabel)

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()