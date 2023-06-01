import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Aktualny indeks rekordu
        self.current_record_index = 0
        self.records = []

        self.initUI()

    def initUI(self):
        # Połącz się z bazą danych
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='xxx'
        )

        # Utwórz kursor
        with connection.cursor() as cursor:
            # Wykonaj zapytanie SQL
            cursor.execute("SELECT * FROM users")

            # Pobierz rekordy
            self.records = cursor.fetchall()

        self.setWindowTitle('Przeglądanie danych MySQL')
        self.setGeometry(300, 300, 300, 200)

        # Przygotuj layout
        layout = QVBoxLayout()

        # Etykieta wyświetlająca rekordy
        self.record_label = QLabel()
        layout.addWidget(self.record_label)

        # Przyciski
        prev_button = QPushButton('Poprzedni')
        prev_button.clicked.connect(self.prev_record)
        next_button = QPushButton('Następny')
        next_button.clicked.connect(self.next_record)

        layout.addWidget(prev_button)
        layout.addWidget(next_button)

        # Utwórz centralny widget dla QMainWindow i ustaw layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Wyświetlaj pierwszy rekord
        self.display_record(self.current_record_index)

    def display_record(self, index):
        id, name, surname, email = self.records[index]
        self.record_label.setText(f"ID: {id}\nImię: {name}\nNazwisko: {surname}\nEmail: {email}")

    def next_record(self):
        if self.current_record_index < len(self.records) - 1:
            self.current_record_index += 1
            self.display_record(self.current_record_index)

    def prev_record(self):
        if self.current_record_index > 0:
            self.current_record_index -= 1
            self.display_record(self.current_record_index)


if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    ex.show()
    app.exec()