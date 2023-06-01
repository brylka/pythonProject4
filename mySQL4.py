import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QWidget


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Aktualny indeks rekordu
        self.current_record_index = 0
        self.records = []

        self.initUI()

    def initUI(self):
        # Połącz się z bazą danych
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='xxx'
        )

        # Pobierz dane z bazy
        self.refresh_data()

        self.setWindowTitle('Przeglądanie danych MySQL')
        self.setGeometry(300, 300, 300, 200)

        # Przygotuj layout
        self.main_layout = QVBoxLayout()

        # Etykieta wyświetlająca rekordy
        self.record_label = QLabel()
        self.main_layout.addWidget(self.record_label)

        # Etykiety dla pól wprowadzania
        self.name_label = QLabel("Imię:")
        self.surname_label = QLabel("Nazwisko:")
        self.email_label = QLabel("Email:")

        # Pola do wprowadzania nowych danych
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Imię")
        self.surname_edit = QLineEdit()
        self.surname_edit.setPlaceholderText("Nazwisko")
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("Email")

        # Przyciski
        self.prev_button = QPushButton('Poprzedni')
        self.prev_button.clicked.connect(self.prev_record)
        self.next_button = QPushButton('Następny')
        self.next_button.clicked.connect(self.next_record)
        self.add_button = QPushButton('Dodaj')
        self.add_button.clicked.connect(self.add_mode)
        self.add_record_button = QPushButton('Dodaj rekord')
        self.add_record_button.clicked.connect(self.add_record)

        self.main_layout.addWidget(self.prev_button)
        self.main_layout.addWidget(self.next_button)
        self.main_layout.addWidget(self.add_button)

        # Utwórz centralny widget dla QMainWindow i ustaw layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

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

    def add_mode(self):
        self.main_layout.removeWidget(self.record_label)
        self.main_layout.removeWidget(self.prev_button)
        self.main_layout.removeWidget(self.next_button)
        self.main_layout.removeWidget(self.add_button)

        self.record_label.hide()
        self.prev_button.hide()
        self.next_button.hide()
        self.add_button.hide()

        self.main_layout.addWidget(self.name_label)
        self.main_layout.addWidget(self.name_edit)
        self.main_layout.addWidget(self.surname_label)
        self.main_layout.addWidget(self.surname_edit)
        self.main_layout.addWidget(self.email_label)
        self.main_layout.addWidget(self.email_edit)
        self.main_layout.addWidget(self.add_record_button)

        self.name_label.show()
        self.name_edit.show()
        self.surname_label.show()
        self.surname_edit.show()
        self.email_label.show()
        self.email_edit.show()
        self.add_record_button.show()

    def add_record(self):
        name = self.name_edit.text()
        surname = self.surname_edit.text()
        email = self.email_edit.text()

        with self.connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO users (name, surname, email) VALUES ('{name}', '{surname}', '{email}')")
            self.connection.commit()

        # Czyszczenie pól wprowadzania po dodaniu rekordu
        self.name_edit.clear()
        self.surname_edit.clear()
        self.email_edit.clear()

        # Odświeżanie rekordów i wyświetlanie ostatnio dodanego
        self.refresh_data()

        self.current_record_index = len(self.records) - 1

        # Powrót do trybu przeglądania
        self.main_layout.removeWidget(self.name_label)
        self.main_layout.removeWidget(self.name_edit)
        self.main_layout.removeWidget(self.surname_label)
        self.main_layout.removeWidget(self.surname_edit)
        self.main_layout.removeWidget(self.email_label)
        self.main_layout.removeWidget(self.email_edit)
        self.main_layout.removeWidget(self.add_record_button)

        self.name_label.hide()
        self.name_edit.hide()
        self.surname_label.hide()
        self.surname_edit.hide()
        self.email_label.hide()
        self.email_edit.hide()
        self.add_record_button.hide()

        self.main_layout.addWidget(self.record_label)
        self.main_layout.addWidget(self.prev_button)
        self.main_layout.addWidget(self.next_button)
        self.main_layout.addWidget(self.add_button)

        self.record_label.show()
        self.prev_button.show()
        self.next_button.show()
        self.add_button.show()

        self.display_record(self.current_record_index)

    def refresh_data(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            self.records = cursor.fetchall()

if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    ex.show()
    app.exec()