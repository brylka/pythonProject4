import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, QMessageBox
from PyQt6.QtCore import QTimer, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test z tabliczki mnożenia")
        self.setGeometry(100, 100, 500, 300)
        self.layout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)
        self.createWidgets()
        self.score = 0
        self.errors = 0
        self.rounds = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.nextRound)
        self.timer.start(10000)  # 10 seconds for each round

    def createWidgets(self):
        self.questionLabel = QLabel(self)
        self.layout.addWidget(self.questionLabel)
        self.answerInput = QLineEdit(self)
        self.layout.addWidget(self.answerInput)
        self.enterButton = QPushButton("Enter", self)
        self.enterButton.clicked.connect(self.checkAnswer)
        self.layout.addWidget(self.enterButton)

    def nextRound(self):
        self.rounds += 1
        if self.rounds > 10:
            self.timer.stop()
            QMessageBox.information(self, "Koniec gry", f"Twój wynik: {self.score} Dobrze, {self.errors} Źle.")
            return
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.questionLabel.setText(f"{self.num1} * {self.num2} = ?")
        self.answerInput.clear()

    def checkAnswer(self):
        try:
            answer = int(self.answerInput.text())
            if answer == self.num1 * self.num2:
                self.score += 1
            else:
                self.errors += 1
            self.nextRound()
        except ValueError:
            QMessageBox.critical(self, "Błąd", "Proszę wprowadzić liczbę.")

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()