import sys
import math
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, \
    QGridLayout, QSpinBox, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Oblicz trójkąt")
        self.setFixedWidth(600)
        self.setFixedHeight(400)

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
        #self.generalLayout.addWidget(self.outputArea)

        self.outputTable = QTableWidget(8, 2)
        #self.outputTable.setHorizontalHeaderLabels(["Atrybuty", "Wartości"])
        self.outputTable.horizontalHeader().setVisible(False)
        self.outputTable.verticalHeader().setVisible(False)
        self.outputTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.outputTable.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        self.outputTable.setColumnWidth(0, 180)
        self.outputTable.setColumnWidth(1, 400)
        self.outputTable.setItem(0, 0, QTableWidgetItem("Obwód"))
        self.outputTable.setItem(1, 0, QTableWidgetItem("Pole"))
        self.outputTable.setItem(2, 0, QTableWidgetItem("Kąty"))
        self.outputTable.setItem(3, 0, QTableWidgetItem("Typ"))
        self.outputTable.setItem(4, 0, QTableWidgetItem("Jest równoboczny"))
        self.outputTable.setItem(5, 0, QTableWidgetItem("Jest równoramienny"))
        self.outputTable.setItem(6, 0, QTableWidgetItem("Promień okręgu wpisanego"))
        self.outputTable.setItem(7, 0, QTableWidgetItem("Promień okręgu opisanego"))
        self.generalLayout.addWidget(self.outputTable)

        self.outputArea.setFixedHeight(100)
        self.outputArea.setFixedWidth(580)
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

                window.outputTable.setItem(0, 1, QTableWidgetItem(str(a + b + c)))
                window.outputTable.setItem(1, 1, QTableWidgetItem(str(area)))
                window.outputTable.setItem(2, 1, QTableWidgetItem(f"{alpha:.3f}, {beta:.3f}, {gamma:.3f}"))
                window.outputTable.setItem(3, 1, QTableWidgetItem(ttype))
                window.outputTable.setItem(4, 1, QTableWidgetItem('tak' if equilateral else 'nie'))
                window.outputTable.setItem(5, 1, QTableWidgetItem('tak' if isosceles else 'nie'))
                window.outputTable.setItem(6, 1, QTableWidgetItem(str(r_inscribed)))
                window.outputTable.setItem(7, 1, QTableWidgetItem(str(r_circumscribed)))
                window.outputArea.setText("")
            else:
                window.outputArea.setText("Nie można obliczyć trójkąta.")
        except ValueError:
            window.outputArea.setText("Błędne dane wejściowe.")

    window.calcButton.clicked.connect(calculate)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()