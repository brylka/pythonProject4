import sys
import math
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, \
    QGridLayout, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Oblicz trójkąt")
        self.setFixedWidth(600)

        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createInterface()

    def _createInterface(self):
        inputLayout = QGridLayout()

        #self.inputFields = [QLineEdit() for _ in range(3)]
        self.inputFields = [QSpinBox() for _ in range(3)]
        for field in self.inputFields:
            field.setRange(0, 1000)
            field.setFixedWidth(100)
        for i, field in enumerate(self.inputFields):
            inputLayout.addWidget(field, 0, i)

        self.calcButton = QPushButton("Oblicz")
        inputLayout.addWidget(self.calcButton, 0, 3)

        self.outputArea = QTextEdit()
        self.outputArea.setReadOnly(True)

        self.generalLayout.addLayout(inputLayout)
        self.generalLayout.addWidget(self.outputArea)

def triangle_area(a, b, c):
    # Pole trójkąta ze wzoru Herona
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def triangle_angles(a, b, c):
    # kąty trójkąta
    alpha = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    beta = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    gamma = math.pi - alpha - beta
    return math.degrees(alpha), math.degrees(beta), math.degrees(gamma)

def triangle_type(a, b, c):
    # typ trójkąta
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return "prostokątny"
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2:
        return "rozwartokątny"
    else:
        return "ostrokątny"

def is_equilateral(a, b, c):
    # czy równoboczny
    return a == b == c

def is_isosceles(a, b, c):
    # czy równoramienny
    return a == b or b == c or c == a

def inscribed_circle_radius(a, b, c, A):
    # r = pole / połowa obwodu
    s = (a + b + c) / 2
    return A / s

def circumscribed_circle_radius(a, b, c, A):
    # R = (abc) / (4 * pole)
    return (a * b * c) / (4 * A)

def main():
    app = QApplication([])

    window = MainWindow()

    def calculate():
        try:
            a, b, c = sorted(float(field.text()) for field in window.inputFields)
            #a, b, c = sorted(field.value() for field in window.inputFields)

            if a + b > c:
                area = triangle_area(a, b, c)
                alpha, beta, gamma = triangle_angles(a, b, c)
                ttype = triangle_type(a, b, c)
                equilateral = is_equilateral(a, b, c)
                isosceles = is_isosceles(a, b, c)
                r_inscribed = inscribed_circle_radius(a, b, c, area)
                r_circumscribed = circumscribed_circle_radius(a, b, c, area)

                window.outputArea.setText(
                    f"Obwód: {a + b + c}\n"
                    f"Pole: {area}\n"
                    f"Kąty: {alpha}, {beta}, {gamma}\n"
                    f"Typ: {ttype}\n"
                    f"Jest równoboczny: {'tak' if equilateral else 'nie'}\n"
                    f"Jest równoramienny: {'tak' if isosceles else 'nie'}\n"
                    f"Promień okręgu wpisanego: {r_inscribed}\n"
                    f"Promień okręgu opisanego: {r_circumscribed}\n"
                )
            else:
                window.outputArea.setText("Nie można obliczyć trójkąta.")
        except ValueError:
            window.outputArea.setText("Błędne dane wejściowe.")

    window.calcButton.clicked.connect(calculate)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()