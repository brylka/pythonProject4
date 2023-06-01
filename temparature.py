from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
import requests
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Tworzenie QLabel do wyświetlania danych pogodowych
        self.temperature_label = QLabel()
        self.temperature_label.setStyleSheet("font-size: 24px; qproperty-alignment: 'AlignCenter';")
        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-size: 10px; qproperty-alignment: 'AlignCenter';")

        layout = QVBoxLayout()
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.time_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Dane pogodowe")
        self.setGeometry(300, 300, 300, 200)

        # Utwórz QTimer, który będzie pobierać dane co minutę
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_weather_data)
        self.timer.start(60000)  # 60000ms = 1 minuta

        # Pobierz dane pogodowe od razu przy uruchomieniu
        self.fetch_weather_data()

    def fetch_weather_data(self):
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Jelenia%20Gora&appid=0ec4c77b4de3d2407f33e949c56bcf31')
        data = response.json()
        temperature = data['main']['temp'] - 273.15  # Konwersja z Kelwinów na Celsjusze
        fetch_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['dt']))
        system_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        self.temperature_label.setText(f"Temperatura: {temperature:.2f} °C")
        self.time_label.setText(f"Czas zarejestrowania danych: {fetch_time}\nCzas pobrania danych z API: {system_time}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()