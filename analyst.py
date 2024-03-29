from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1192, 609)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    border-image: url(:/newPrefix/hinh/analysis1.png);\n"
"background-color: rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dumbell = QtWidgets.QPushButton(self.centralwidget)
        self.dumbell.setGeometry(QtCore.QRect(30, 130, 221, 91))
        self.dumbell.setMinimumSize(QtCore.QSize(0, 0))
        self.dumbell.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dumbell.setFont(font)
        self.dumbell.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.dumbell.setObjectName("dumbell")
        self.yoga = QtWidgets.QPushButton(self.centralwidget)
        self.yoga.setGeometry(QtCore.QRect(30, 240, 221, 81))
        self.yoga.setToolTip("")
        self.yoga.setWhatsThis("")
        self.yoga.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.yoga.setObjectName("yoga")
        self.view = QtWidgets.QLabel(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(270, 130, 600, 450))
        self.view.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.view.setText("")
        self.view.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.view.setWordWrap(False)
        self.view.setObjectName("view")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 470, 221, 51))
        self.back.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.back.setObjectName("back")
        self.information = QtWidgets.QLabel(self.centralwidget)
        self.information.setGeometry(QtCore.QRect(890, 130, 261, 241))
        self.information.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.information.setText("")
        self.information.setObjectName("information")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1030, 450, 111, 91))
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(870, 470, 121, 61))
        self.label_2.setStyleSheet("border-color: rgb(255, 170, 0);\n"
"font: 45 48pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"font:30pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(1030, 390, 121, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.timeLabel.setObjectName("timeLabel")
        self.information_2 = QtWidgets.QLabel(self.centralwidget)
        self.information_2.setGeometry(QtCore.QRect(750, 460, 111, 101))
        self.information_2.setStyleSheet("border-image: url(:/newPrefix/yoga/2.jpg);")
        self.information_2.setText("")
        self.information_2.setObjectName("information_2")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(890, 390, 91, 51))
        self.start.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dumbell.setText(_translate("MainWindow", "DUMBBELL\n"
" SHOULDER PRESS"))
        self.yoga.setText(_translate("MainWindow", "YOGA"))
        self.back.setText(_translate("MainWindow", "BACK"))
        self.label_2.setText(_translate("MainWindow", " REP"))
        self.timeLabel.setText(_translate("MainWindow", "00:00"))
        self.start.setText(_translate("MainWindow", "STOP"))
import yoga1_rc
