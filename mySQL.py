import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget


class App(QMainWindow):
    def __init__(self):
        super().__init__()

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
            records = cursor.fetchall()

        self.setWindowTitle('Przeglądanie danych MySQL')
        self.setGeometry(300, 300, 300, 200)

        # Przygotuj layout
        layout = QVBoxLayout()

        # Wyświetlaj rekordy
        for record in records:
            id_, name, surname, email = record
            record_label = QLabel(f"ID: {id_}, Imię: {name}, Nazwisko: {surname}, Email: {email}")
            layout.addWidget(record_label)

        # Utwórz centralny widget dla QMainWindow i ustaw layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    ex.show()
    app.exec()