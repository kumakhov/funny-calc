import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from interface.calc import Calculator


# execute app and show window
# запуск приложения и показ окна
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec())
