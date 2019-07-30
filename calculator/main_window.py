import operator

from PySide2.QtWidgets import QMainWindow

from .main_window_ui import Ui_MainWindow

from decimal import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.num_first = None
        self.num_second = None
        self.operation = None
        self.output = 0

        self.buttons = [
            self.btn_0,
            self.btn_1,
            self.btn_2,
            self.btn_3,
            self.btn_4,
            self.btn_5,
            self.btn_6,
            self.btn_7,
            self.btn_8,
            self.btn_9
        ]

        self.func_buttons = [
            self.btn_add,
            self.btn_divide,
            self.btn_multiply,
            self.btn_subtract
        ]

        # by clicked on button '.' add and show point to current number
        self.btn_point.clicked.connect(self.clicked_point)

        # by clicked on button 'AC' clear output line
        self.btn_clear.clicked.connect(self.clear_screen)

        # by clicked on button '=' show result of the calculation
        self.btn_equal.clicked.connect(self.calculation)

        for button in self.buttons:
            button.clicked.connect(self.clicked_number_btn)

        for func_btn in self.func_buttons:
            func_btn.clicked.connect(self.clicked_function_btn)

        # by clicked on button '+/-' convert current number to otherwise
        self.inversion_btn.clicked.connect(self.converted_number)

        # by clicked on button '%' calculate percentage
        self.btn_percent.clicked.connect(self.calculate_percentage)

    def clicked_number_btn(self):
        # by clicked button via signal get current number
        digit = self.sender().text()

        if self.operation is None:
            # redirect this number to output line
            if self.output_line.text() == '0':
                self.num_first = digit
                self.output_line.setText(digit)
                print(self.num_first)
            else:
                # add next digit to output line
                self.num_first = self.output_line.text() + digit
                self.output_line.setText(self.num_first)
                print(self.num_first)
        else:
            if self.num_second is None:
                self.output_line.setText('')
                self.num_second = digit
                self.output_line.setText(self.num_second)
                print(self.num_second)
            else:
                self.num_second = self.output_line.text() + digit
                self.output_line.setText(self.num_second)
                print(self.num_second)

    def clicked_function_btn(self):
        if self.num_second is not None:
            self.calculation()

            self.output_line.setText(self.output)

            self.num_first = self.output
            self.num_second = None

            self.operation = self.sender().text()
            print(self.operation)
        else:
            self.operation = self.sender().text()
            print(self.operation)

    def calculation(self):
        if self.operation == '+':
            self.math_function(operator.add)
        elif self.operation == '-':
            self.math_function(operator.sub)
        elif self.operation == '/':
            self.math_function(operator.truediv)
        elif self.operation == '*':
            self.math_function(operator.mul)

    def math_function(self, op):
        print('FIRST NUM ==>', self.num_first)
        print('SECOND NUM ==>', self.num_second)

        if self.num_first is not None and self.operation is not None and self.num_second is None:
            first = Decimal(self.num_first)
            self.output = str(op(first, first))

            self.num_second = self.num_first
            self.num_first = self.output
        else:
            first = Decimal(self.num_first)
            second = Decimal(self.num_second)
            self.output = str(op(first, second))

            self.num_first = self.output

        self.output_line.setText(self.output)

    def calculate_percentage(self):
        if self.num_first is not None and self.num_second is not None and self.operation is not None:
            self.output = (Decimal(self.num_first) * Decimal(self.num_second)) / 100
            self.output_line.setText(str(self.output))
            self.num_second = self.output

    # add point '.' to current number in output line
    def clicked_point(self):
        text = self.output_line.text()
        res = ''

        if '.' not in text:
            res = text + '.'

        if self.operation is None:
            self.num_first = res
        else:
            self.num_second = res

        self.output_line.setText(res)

    # convert current number to negative or positive value
    def converted_number(self):
        text = self.output_line.text()
        value = float(text)

        if value > 0:
            text = '-' + text
            print(text)
        else:
            text = text[1:]
            print(text)

        if self.operation is None:
            self.num_first = text
        else:
            self.num_second = text

        self.output_line.setText(text)

    def clear_screen(self):
        self.output_line.setText('0')
        self.num_first = None
        self.num_second = None
        self.operation = None
        self.output = 0
