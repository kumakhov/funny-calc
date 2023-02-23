from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # окошко калькулятора (цифры которые показывает)
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)

        # создание сетки для кнопок
        layout = QGridLayout()
        layout.addWidget(self.display, 0, 0, 1, 5)

        self.setLayout(layout)
        self.show()
        # установка названия окна

        # вот этот прикол добавляет кнопки и вставялет их в слоты (не казино)
        btn_7 = QPushButton("7")
        btn_7.clicked.connect(lambda: self.append_number("7"))
        layout.addWidget(btn_7, 1, 0)

        btn_8 = QPushButton("8")
        btn_8.clicked.connect(lambda: self.append_number("8"))
        layout.addWidget(btn_8, 1, 1)

        btn_9 = QPushButton("9")
        btn_9.clicked.connect(lambda: self.append_number("9"))
        layout.addWidget(btn_9, 1, 2)

        btn_add = QPushButton("+")
        btn_add.clicked.connect(lambda: self.append_number("+"))
        layout.addWidget(btn_add, 1, 3)

        btn_clear = QPushButton("C")
        btn_clear.clicked.connect(self.clear)
        layout.addWidget(btn_clear, 1, 4)

        btn_4 = QPushButton("4")
        btn_4.clicked.connect(lambda: self.append_number("4"))
        layout.addWidget(btn_4, 2, 0)

        btn_5 = QPushButton("5")
        btn_5.clicked.connect(lambda: self.append_number("5"))
        layout.addWidget(btn_5, 2, 1)

        btn_6 = QPushButton("6")
        btn_6.clicked.connect(lambda: self.append_number("6"))
        layout.addWidget(btn_6, 2, 2)

        btn_sub = QPushButton("-")
        btn_sub.clicked.connect(lambda: self.append_number("-"))
        layout.addWidget(btn_sub, 2, 3)

        btn_back = QPushButton("<-")
        btn_back.clicked.connect(self.backspace)
        layout.addWidget(btn_back, 2, 4)

        btn_1 = QPushButton("1")
        btn_1.clicked.connect(lambda: self.append_number("1"))
        layout.addWidget(btn_1, 3, 0)

        btn_2 = QPushButton("2")
        btn_2.clicked.connect(lambda: self.append_number("2"))
        layout.addWidget(btn_2, 3, 1)

        btn_3 = QPushButton("3")
        btn_3.clicked.connect(lambda: self.append_number("3"))
        layout.addWidget(btn_3, 3, 2)

        btn_0 = QPushButton("0")
        btn_0.clicked.connect(lambda: self.append_number("0"))
        layout.addWidget(btn_0, 4, 0)

        btn_00 = QPushButton("00")
        btn_00.clicked.connect(lambda: self.append_number("00"))
        layout.addWidget(btn_00, 4, 1)

        btn_mul = QPushButton("*")
        btn_mul.clicked.connect(lambda: self.append_number("*"))
        layout.addWidget(btn_mul, 4, 2)

        btn_div = QPushButton("/")
        btn_div.clicked.connect(lambda: self.append_number("/"))
        layout.addWidget(btn_div, 3, 3)

        btn_eval = QPushButton("=")
        btn_eval.clicked.connect(self.evaluate)
        layout.addWidget(btn_eval, 4, 3)

    # выводит нажатую цифру в окошко
    def append_number(self, num):
        current_text = self.display.text()
        self.display.setText(current_text + num)

    # этот прикол очищает окошко
    def clear(self):
        self.display.setText("")

    # убирает последнюю цифру с дисплея
    def backspace(self):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])

    # вычисление
    def evaluate(self):
        current_text = self.display.text()
        try:
            result = eval(current_text)
            self.display.setText(str(result))
        except:
            self.display.setText("Error")
