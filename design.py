# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setObjectName("back")
        self.gridLayout_2.addWidget(self.back, 0, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.main)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 5, 1, 1, 1)
        self.kvadrati = QtWidgets.QRadioButton(self.main)
        self.kvadrati.setObjectName("kvadrati")
        self.shape_group = QtWidgets.QButtonGroup(MainWindow)
        self.shape_group.setObjectName("shape_group")
        self.shape_group.addButton(self.kvadrati)
        self.gridLayout_3.addWidget(self.kvadrati, 4, 1, 1, 1)
        self.trapecia = QtWidgets.QRadioButton(self.main)
        self.trapecia.setObjectName("trapecia")
        self.shape_group.addButton(self.trapecia)
        self.gridLayout_3.addWidget(self.trapecia, 3, 1, 1, 1)
        self.samkutxedi = QtWidgets.QRadioButton(self.main)
        self.samkutxedi.setObjectName("samkutxedi")
        self.shape_group.addButton(self.samkutxedi)
        self.gridLayout_3.addWidget(self.samkutxedi, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 0, 1, 1)
        self.wre = QtWidgets.QRadioButton(self.main)
        self.wre.setAutoExclusive(True)
        self.wre.setObjectName("wre")
        self.shape_group.addButton(self.wre)
        self.gridLayout_3.addWidget(self.wre, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 2, 1, 1)
        self.select = QtWidgets.QPushButton(self.main)
        self.select.setObjectName("select")
        self.gridLayout_3.addWidget(self.select, 5, 2, 1, 1)
        self.stackedWidget.addWidget(self.main)
        self.samkutxedi_page = QtWidgets.QWidget()
        self.samkutxedi_page.setObjectName("samkutxedi_page")
        self.label_4 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_4.setGeometry(QtCore.QRect(150, 16, 71, 31))
        self.label_4.setObjectName("label_4")
        self.s1 = QtWidgets.QDoubleSpinBox(self.samkutxedi_page)
        self.s1.setGeometry(QtCore.QRect(280, 10, 151, 41))
        self.s1.setObjectName("s1")
        self.label_5 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_5.setGeometry(QtCore.QRect(150, 70, 71, 31))
        self.label_5.setObjectName("label_5")
        self.s2 = QtWidgets.QDoubleSpinBox(self.samkutxedi_page)
        self.s2.setGeometry(QtCore.QRect(280, 60, 151, 41))
        self.s2.setObjectName("s2")
        self.label_6 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_6.setGeometry(QtCore.QRect(150, 120, 71, 31))
        self.label_6.setObjectName("label_6")
        self.s3 = QtWidgets.QDoubleSpinBox(self.samkutxedi_page)
        self.s3.setGeometry(QtCore.QRect(280, 110, 151, 41))
        self.s3.setObjectName("s3")
        self.label_7 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_7.setGeometry(QtCore.QRect(260, 270, 101, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_8.setGeometry(QtCore.QRect(260, 320, 111, 17))
        self.label_8.setObjectName("label_8")
        self.lcd_s_area = QtWidgets.QLCDNumber(self.samkutxedi_page)
        self.lcd_s_area.setGeometry(QtCore.QRect(390, 270, 64, 23))
        self.lcd_s_area.setObjectName("lcd_s_area")
        self.lcd_s_perimeter = QtWidgets.QLCDNumber(self.samkutxedi_page)
        self.lcd_s_perimeter.setGeometry(QtCore.QRect(390, 320, 64, 23))
        self.lcd_s_perimeter.setObjectName("lcd_s_perimeter")
        self.stackedWidget.addWidget(self.samkutxedi_page)
        self.wre_page = QtWidgets.QWidget()
        self.wre_page.setObjectName("wre_page")
        self.r1 = QtWidgets.QDoubleSpinBox(self.wre_page)
        self.r1.setGeometry(QtCore.QRect(220, 30, 151, 41))
        self.r1.setObjectName("r1")
        self.label = QtWidgets.QLabel(self.wre_page)
        self.label.setGeometry(QtCore.QRect(126, 36, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.wre_page)
        self.label_2.setGeometry(QtCore.QRect(130, 200, 121, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.wre_page)
        self.label_3.setGeometry(QtCore.QRect(130, 260, 67, 17))
        self.label_3.setObjectName("label_3")
        self.lcd_r_area = QtWidgets.QLCDNumber(self.wre_page)
        self.lcd_r_area.setGeometry(QtCore.QRect(230, 200, 64, 23))
        self.lcd_r_area.setObjectName("lcd_r_area")
        self.lcd_r_perimeter = QtWidgets.QLCDNumber(self.wre_page)
        self.lcd_r_perimeter.setGeometry(QtCore.QRect(230, 260, 64, 23))
        self.lcd_r_perimeter.setObjectName("lcd_r_perimeter")
        self.stackedWidget.addWidget(self.wre_page)
        self.trapecia_page = QtWidgets.QWidget()
        self.trapecia_page.setObjectName("trapecia_page")
        self.checkBox = QtWidgets.QCheckBox(self.trapecia_page)
        self.checkBox.setGeometry(QtCore.QRect(330, 230, 92, 23))
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.trapecia_page)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 0, 1, 1)
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setObjectName("calculate")
        self.gridLayout_2.addWidget(self.calculate, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


                # Square  Page
        self.kvadrati_page = QtWidgets.QWidget()
        self.kvadrati_page.setObjectName("kvadrati_page")
        self.kvadrati_side = QtWidgets.QDoubleSpinBox(self.kvadrati_page)
        self.kvadrati_side.setGeometry(QtCore.QRect(280, 100, 151, 41))  
        self.kvadrati_side.setObjectName("kvadrati_side")
        self.lcd_kvadrati_area = QtWidgets.QLCDNumber(self.kvadrati_page)
        self.lcd_kvadrati_area.setGeometry(QtCore.QRect(390, 270, 64, 23))
        self.lcd_kvadrati_area.setObjectName("lcd_kvadrati_area")
        self.lcd_kvadrati_perimeter = QtWidgets.QLCDNumber(self.kvadrati_page)
        self.lcd_kvadrati_perimeter.setGeometry(QtCore.QRect(390, 320, 64, 23))
        self.lcd_kvadrati_perimeter.setObjectName("lcd_kvadrati_perimeter")
        self.stackedWidget.addWidget(self.kvadrati_page)


                # Trapezoid  Page
        self.trapecia_page = QtWidgets.QWidget()
        self.trapecia_page.setObjectName("trapecia_page")
        self.trapecia_base1 = QtWidgets.QDoubleSpinBox(self.trapecia_page)
        self.trapecia_base1.setGeometry(QtCore.QRect(280, 60, 151, 41))  
        self.trapecia_base1.setObjectName("trapecia_base1")
        self.trapecia_base2 = QtWidgets.QDoubleSpinBox(self.trapecia_page)
        self.trapecia_base2.setGeometry(QtCore.QRect(280, 110, 151, 41))  
        self.trapecia_base2.setObjectName("trapecia_base2")
        self.trapecia_height = QtWidgets.QDoubleSpinBox(self.trapecia_page)
        self.trapecia_height.setGeometry(QtCore.QRect(280, 160, 151, 41))  
        self.trapecia_height.setObjectName("trapecia_height")
        self.lcd_trapecia_area = QtWidgets.QLCDNumber(self.trapecia_page)
        self.lcd_trapecia_area.setGeometry(QtCore.QRect(390, 270, 64, 23))
        self.lcd_trapecia_area.setObjectName("lcd_trapecia_area")
        self.stackedWidget.addWidget(self.trapecia_page)


        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back.setText(_translate("MainWindow", "უკან დაბრუნება"))
        self.kvadrati.setText(_translate("MainWindow", "კვადრატი"))
        self.trapecia.setText(_translate("MainWindow", "ტრაპეცია"))
        self.samkutxedi.setText(_translate("MainWindow", "სამკუთხედი"))
        self.wre.setText(_translate("MainWindow", "წრე"))
        self.select.setText(_translate("MainWindow", "არჩევა"))
        self.label_4.setText(_translate("MainWindow", "გვერდი1"))
        self.label_5.setText(_translate("MainWindow", "გვერდი2"))
        self.label_6.setText(_translate("MainWindow", "გვერდი3"))
        self.label_7.setText(_translate("MainWindow", "ფართობი"))
        self.label_8.setText(_translate("MainWindow", "პერიმეტრი"))
        self.label.setText(_translate("MainWindow", "რადიუსი"))
        self.label_2.setText(_translate("MainWindow", "ფართობი"))
        self.label_3.setText(_translate("MainWindow", "სიგრძე"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.calculate.setText(_translate("MainWindow", "გამოთვლა"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
