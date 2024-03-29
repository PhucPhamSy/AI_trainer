from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 609)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    border-image: url(:/newPrefix/hinh/CPENT.png);\n"
"background-color: rgb(0, 255, 255);\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.count = QtWidgets.QPushButton(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(450, 210, 291, 71))
        self.count.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.count.setObjectName("count")
        self.analys = QtWidgets.QPushButton(self.centralwidget)
        self.analys.setGeometry(QtCore.QRect(450, 330, 291, 71))
        self.analys.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.analys.setObjectName("analys")
        self.cadio = QtWidgets.QPushButton(self.centralwidget)
        self.cadio.setGeometry(QtCore.QRect(450, 450, 291, 71))
        self.cadio.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.cadio.setObjectName("cadio")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.count.setText(_translate("MainWindow", "COUNT REP"))
        self.analys.setText(_translate("MainWindow", "ANALYSIS"))
        self.cadio.setText(_translate("MainWindow", "CARDIO"))
import yoga1_rc
