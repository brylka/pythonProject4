from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Tworzenie akcji, które będą wykorzystane w menu
        hello_action = QAction("Hello", self)
        hello_action.triggered.connect(self.hello)

        # Tworzenie menu
        main_menu = self.menuBar()

        # Dodanie menu "Plik"
        file_menu = main_menu.addMenu("Plik")
        file_menu.addAction(hello_action)

        # Dodanie akcji "Widok" bez rozwijanego menu
        tadam_action = QAction("Widok", self)
        tadam_action.triggered.connect(self.tadam)
        main_menu.addAction(tadam_action)

        # Dodanie menu "Pomoc"
        help_menu = main_menu.addMenu("Pomoc")

        self.setWindowTitle("Menu w Qt6")
        #self.setGeometry(300, 300, 300, 200)
        self.resize(300, 200)

        # Dodanie wisgetu, w którym będzie pojawiał się tekst
        self.message_label = QLabel()
        self.message_label.setStyleSheet("font-size: 18px; qproperty-alignment: 'AlignCenter';")
        layout = QVBoxLayout()
        layout.addWidget(self.message_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def hello(self):
        self.message_label.setText("Witaj Świecie!")

    def tadam(self):
        self.message_label.setText("Tadam!")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()