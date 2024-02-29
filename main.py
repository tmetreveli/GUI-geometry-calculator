import sys
from PyQt5 import QtWidgets
from design import Ui_MainWindow  
import math

class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.main)
        self.select.clicked.connect(self.select_shape)
        self.back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main))
        self.calculate.clicked.connect(self.perform_calculation)

    def select_shape(self):
        shape_name = self.shape_group.checkedButton().objectName()
        self.stackedWidget.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main)
        )

    def perform_calculation(self):
        shape_name = self.shape_group.checkedButton().objectName()
        if shape_name == "wre":
            self.calculate_circle()
        elif shape_name == "samkutxedi":
            self.calculate_triangle()
        elif shape_name == "kvadrati":
            self.calculate_square()
        elif shape_name == "trapecia":
            self.calculate_trapecia()

    def calculate_circle(self):
        radius = self.r1.value()
        area = math.pi * radius ** 2
        perimeter = 2 * math.pi * radius
        self.lcd_r_area.display(area)
        self.lcd_r_perimeter.display(perimeter)

    def calculate_triangle(self):
        a = self.s1.value()
        b = self.s2.value()
        c = self.s3.value()
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        self.lcd_s_area.display(area)
        self.lcd_s_perimeter.display(perimeter)

    def calculate_square(self):
        side_length = self.kvadrati_side.value()
        area = side_length ** 2
        perimeter = 4 * side_length
        self.lcd_kvadrati_area.display(area)
        self.lcd_kvadrati_perimeter.display(perimeter)

    def calculate_trapecia(self):
        base1 = self.trapecia_base1.value()
        base2 = self.trapecia_base2.value()
        height = self.trapecia_height.value()
        area = (base1 + base2) / 2 * height
        self.lcd_trapecia_area.display(area)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec_())
