import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # create the display for the calculator
        # окошко калькулятора (цифры которые показывает)
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)

        # create a grid layout for buttons
        # создание сетки для кнопок
        layout = QGridLayout()
        layout.addWidget(self.display, 0, 0, 1, 5)

        self.setLayout(layout)
        self.show()

        # set the window title
        # установка названия окна
        self.setWindowTitle("Смешной калькулятор")


# execute app and show window
# запуск приложения и показ окна
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec())
