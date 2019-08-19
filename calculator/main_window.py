from decimal import Decimal, DivisionByZero
import operator

from PySide2.QtGui import QFontMetrics
from PySide2.QtWidgets import QMainWindow

from .main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(319, 410)

        self.num_first = ''
        self.num_second = ''
        self.operation = None
        self.current_num = ''
        self.output = 0
        # set flag for clicked on button '='
        self.equal_pressed = False

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

        if self.operation is None and self.equal_pressed is False:
            # redirect this number to output line
            if self.output_line.text() == '0':
                self.num_first = digit
                self.display_number_on_screen(digit)
                print(self.num_first)
            else:
                # add next digit to output line
                self.num_first = self.num_first + digit
                self.display_number_on_screen(self.num_first)
                print(self.num_first)
        elif (self.operation is not None and
              self.num_second != '' and self.equal_pressed is True):
            if self.num_first == self.output:
                self.num_first = ''
                self.num_first = digit
                self.display_number_on_screen(self.num_first)
                print(self.num_first)
            else:
                self.num_first = self.num_first + digit
                self.display_number_on_screen(self.num_first)
                print(self.num_first)
        else:
            if self.num_second == '':
                self.output_line.setText('')
                self.num_second = digit
                self.display_number_on_screen(self.num_second)
                print(self.num_second)
                self.equal_pressed = False
            else:
                self.num_second = self.num_second + digit
                self.display_number_on_screen(self.num_second)
                print(self.num_second)

    def clicked_function_btn(self):
        if self.equal_pressed is False:
            if self.num_second != '':
                self.calculation()

                self.num_first = self.output_line.text()
                self.num_second = ''

                self.operation = self.sender().text()
                print(self.operation)
            else:
                self.operation = self.sender().text()
                print(self.operation)
        elif self.equal_pressed is True:
            if self.num_first != '':
                self.operation = self.sender().text()
                print(self.operation)

                self.num_second = ''

    def calculation(self):
        if self.operation == '+':
            self.math_function(operator.add)
        elif self.operation == '-':
            self.math_function(operator.sub)
        elif self.operation == '/':
            self.math_function(operator.truediv)
        elif self.operation == '*':
            self.math_function(operator.mul)

        self.equal_pressed = True

    def math_function(self, op):
        print('FIRST NUM ==>', self.num_first)
        print('SECOND NUM ==>', self.num_second)
        try:
            if (self.num_first != '' and
                    self.operation is not None and
                    self.num_second == ''):
                first = Decimal(self.num_first)
                self.output = str(op(first, first))

                self.num_second = self.num_first
                self.num_first = self.output
            else:
                first = Decimal(self.num_first)
                second = Decimal(self.num_second)
                self.output = str(op(first, second))

                self.num_first = self.output

            self.display_number_on_screen(self.output)

        except DivisionByZero:
            self.output_line.setText('Dividing a number by zero')

    def calculate_percentage(self):
        if (self.num_first != '' and
                self.num_second != '' and
                self.operation is not None):
            self.output = (
                (Decimal(self.num_first) * Decimal(self.num_second)) / 100)
            self.display_number_on_screen(str(self.output))
            self.num_second = self.output

    # add point '.' to current number in output line
    def clicked_point(self):
        if '.' not in self.current_num:
            self.output = self.current_num + '.'
        else:
            self.output = self.current_num

        if self.operation is None:
            self.num_first = self.output
        else:
            self.num_second = self.output

        self.display_number_on_screen(self.output)

    # convert current number to negative or positive value
    def converted_number(self):
        self.output = self.current_num
        value = float(self.output)

        if value > 0:
            self.output = '-' + self.output
            print(self.output)
        elif value == 0:
            self.output = self.output
        else:
            self.output = self.output[1:]
            print(self.output)

        if self.equal_pressed is True:
            self.num_first = self.output

        if self.operation is None:
            self.num_first = self.output
        else:
            self.num_second = self.output

        self.display_number_on_screen(self.output)

    # processing the display of numbers on the screen
    def display_number_on_screen(self, value):
        self.current_num = value

        output = f'{Decimal(value):,}'

        # calculate width for input line
        window_width = (self.output_line.width()) - 10

        # get font information for current text input
        font = self.output_line.font()

        for i in range(30, 7, -1):
            font.setPointSize(i)
            # calculate width for current line
            output_width = QFontMetrics(font).width(output)

            if output_width < window_width:
                self.output_line.setFont(font)
                break

        self.output_line.setText(output)

    def clear_screen(self):
        self.display_number_on_screen(0)
        self.equal_pressed = False
        self.num_first = ''
        self.num_second = ''
        self.current_num = ''
        self.operation = None
        self.output = 0
