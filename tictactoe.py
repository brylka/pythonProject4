from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox
from PyQt6.QtCore import QSize, Qt
import sys

# Definicja głównej klasy gry TicTacToe, dziedziczącej po QWidget
class TicTacToe(QWidget):
    def __init__(self):
        super(TicTacToe, self).__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setMinimumSize(QSize(300, 300))  # Ustawienie minimalnej wielkości okna
        self.board = [['' for _ in range(3)] for _ in range(3)]  # Inicjalizacja pustej planszy gry
        self.current_player = 'X'  # Ustawienie 'X' jako gracza, który zaczyna grę
        self.end_game = False  # Flaga informująca, czy gra została zakończona
        self.initUI()  # Wywołanie metody inicjalizującej interfejs użytkownika

    # Metoda inicjalizująca interfejs użytkownika
    def initUI(self):
        self.layout = QGridLayout()  # Utworzenie siatki do rozmieszczenia przycisków
        self.buttons = []  # Lista przechowująca przyciski

        # Utworzenie 9 przycisków (3x3), każdy przycisk połączony jest z funkcją make_move
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton()
                button.setCheckable(True)
                button.setFixedSize(QSize(80, 80))  # Ustawienie rozmiaru przycisku
                button.clicked.connect(lambda _, x=i, y=j: self.make_move(x, y))  # Połączenie przycisku z funkcją make_move
                self.layout.addWidget(button, i, j)  # Dodanie przycisku do layoutu
                row.append(button)
            self.buttons.append(row)
        self.setLayout(self.layout)

    # Metoda wywoływana, gdy gracz klika na przycisk (pole gry)
    def make_move(self, x, y):
        if not self.end_game and self.board[x][y] == '':  # Jeśli gra nie jest zakończona i pole jest puste
            self.board[x][y] = self.current_player  # Przypisz pole do obecnego gracza
            self.buttons[x][y].setText(self.current_player)  # Wyświetl znak gracza na przycisku
            # Sprawdź, czy obecny gracz wygrał
            if self.check_win(self.current_player):
                QMessageBox.information(self, "Koniec gry", f"Gracz {self.current_player} wygrywa!")
                self.end_game = True
            # Sprawdź, czy plansza jest pełna (remis)
            elif '' not in [self.board[i][j] for i in range(3) for j in range(3)]:
                QMessageBox.information(self, "Koniec gry", "Remis!")
                self.end_game = True
            # Jeżeli gra nadal trwa, zmień gracza
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

                # Metoda sprawdzająca, czy obecny gracz wygrał

    def check_win(self, player):
        # Lista wszystkich możliwych kombinacji wygrywających
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]]
        ]
        # Jeżeli którakolwiek z wygrywających kombinacji jest na planszy, gracz wygrywa
        return [player, player, player] in win_conditions

app = QApplication(sys.argv)  # Utworzenie instancji aplikacji PyQt
window = TicTacToe()  # Utworzenie instancji naszej klasy gry TicTacToe
window.show()  # Wyświetlenie okna gry
sys.exit(app.exec())  # Rozpoczęcie głównej pętli aplikacji