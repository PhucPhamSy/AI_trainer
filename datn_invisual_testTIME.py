
from PyQt5 import QtGui, QtWidgets, QtCore
import sys, time, threading, home, count, analyst, cardio, demtg, playsound, winsound
import barbell_cruls as bc
import dumbbell_shoulder as ds
import yoga
import texttime as tt


ui = ''
cp = 0
img = ''
flagRight = 1  
check = False  
check2 = False 
giay_tt = False

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setFixedSize(1173, 609)

def test():
	import os
	os._exit(0)

app.aboutToQuit.connect(test)

tt.init()


def mainUi():
	global ui, cp
	playS("sound\\Button_1_down.wav", 0)  # am thanh ban phim
	playS("sound\\intro.wav", 1)  # intro
	cp = 0
	bc.init(0)
	ds.init(0)
	yoga.init(0)
	ui = home.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.count.clicked.connect(countUi)
	ui.analys.clicked.connect(analystUi)
	ui.cadio.clicked.connect(cardioUi)
	MainWindow.show()


def countUi():
	global ui
	playS("sound\\Button_1_down.wav", 0)
	playS("sound\\task_beat.wav", 1)  # 0 :0 lap lai   1: lap lai
	#
	ui = count.Ui_MainWindow()
	ui.setupUi(MainWindow)

	# phim chuc nang
	ui.back.clicked.connect(mainUi)
	ui.abs.clicked.connect(lambda: count_task(1))
	ui.curls.clicked.connect(lambda: count_task(2))
	ui.squats.clicked.connect(lambda: count_task(3))
	ui.pushup.clicked.connect(lambda: count_task(4))
	ui.start.clicked.connect(stop)  # phim stop

	# tac chuc nang chon RIGHT LEFT
	ui.radioL.setVisible(False)
	ui.radioR.setVisible(False)

	MainWindow.show()


def analystUi():
	global ui, check2
	playS("sound\\Button_1_down.wav", 0)
	playS("sound\\task_beat.wav", 1)
	ui = analyst.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.back.clicked.connect(mainUi)
	ui.dumbell.clicked.connect(analyst_task)
	ui.yoga.clicked.connect(yoga_task)
	ui.information_2.setVisible(False)
	ui.start.clicked.connect(stop)  # phim stop
	#check2 = True

	MainWindow.show()


def cardioUi():
	global ui, rep
	playS("sound\\Button_1_down.wav", 0)
	playS("sound\\task_beat.wav", 1)
	ui = cardio.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.back.clicked.connect(mainUi)
	ui.beginner.clicked.connect(cardio_task)
	rep = 0
	MainWindow.show()



def stop():
	global ui, cp
	playS("sound\\Button_1_down.wav", 0)
	playS("sound\\task_beat.wav", 1)
	cp = 0
	bc.init(0)
	ds.init(0)
	yoga.init(0)
	ui.view.setStyleSheet("background-color: rgb(157, 157, 157);")
	ui.view.setText(" ")
	ui.information.setStyleSheet("background-color: rgb(157, 157, 157);")
	ui.information.setText(" ")


# COUNT_REP
def count_task(z):  # z la chuc nang duoc quy dinh trong form COUNT_REP
	# #func (function): lay chuc nang trong thu vien barbell_cruls
	global cp, func, giay_tt
	playS("sound\\Button_1_down.wav", 0)
	playS("sound\\count.wav", 1)
	cp = 0
	bc.init(0)
	time.sleep(0.1)
	bc.init(1)
	cp = 1
	tt.giay = 0
	giay_tt = False
	if (z == 1):
		func = 2
		ui.radioL.setVisible(False)
		ui.radioR.setVisible(False)
	elif (z == 2):
		func = 1
		ui.radioL.setVisible(True)
		ui.radioR.setVisible(True)
		ui.radioR.setChecked(True)
	elif (z == 3):
		func = 3
		ui.radioL.setVisible(False)
		ui.radioR.setVisible(False)
	elif (z == 4):
		func = 4
		ui.radioL.setVisible(False)
		ui.radioR.setVisible(False)



def analyst_task():
	global cp
	# playS("sound\\Button_1_down.wav", 0)
	# playS("sound\\Abandon Ship.wav", 1)
	playS("sound\\Button_1_down.wav", 0)
	playS("sound\\count.wav", 1)
	cp = 0
	ds.init(0)
	time.sleep(0.1)
	ds.init(1)
	cp = 2
	tt.giay = 0


def yoga_task():
	global cp, check2
	playS("sound\\Button_1_down.wav", 0)
	playS("sound\\task.wav", 1)
	cp = 0
	yoga.init(0)
	time.sleep(0.1)
	yoga.init(1)
	cp = 3
	check2 = True



def cardio_task():
	global cp, phut_tt
	playS("sound\\Button_1_down.wav", 0)
	playS("sound\\cardio.wav", 1)
	cp = 0
	yoga.init(0)
	time.sleep(0.1)
	yoga.init(1)
	cp = 4
	tt.giay = tt.phut = 0
	phut_tt = False



def hienhinh(a, b, per):
	if (per <= 20):
		
		image_path = "" + a 
		image_profile = QtGui.QImage(image_path)  
		image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
											 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))

	elif (per >= 90):

		image_path = "" + b  # path to your image file
		image_profile = QtGui.QImage(image_path)  
		image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
											 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))


def hienhinh_cardio(a, b, giay, thoigiantap):
	global check2
	if (giay < thoigiantap):
	
		image_path = "hinh\\" + a  

		image_profile = QtGui.QImage(image_path)  
		image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
											 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))
		check2 = True

	elif (giay > thoigiantap):

		image_path = "hinh\\" + b
		image_profile = QtGui.QImage(image_path)  
		image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
											 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))



def main():
	global img, ui, rep, func, flagRight, check, dem, yoga_hinh, phut_tt, check2
	print("bat luong")
	while True:

		#  chuc nang FORM COUNT_REP
		if cp == 1:
			# xet truong hop barbell_curls trai phai
			if func < 2:
				if (ui.radioR.isChecked() and flagRight == 1):
					flagRight = 0
					func = 1  # barbell_curls  Right_arm
					bc.count = 0
					playS("sound\\Button_1_down.wav", 0)
					playS("sound\\count.wav", 1)
				elif (ui.radioL.isChecked() and flagRight == 0):
					flagRight = 1
					func = 0  ## barbell_curls  Left_arm
					bc.count = 0
					playS("sound\\Button_1_down.wav", 0)
					playS("sound\\count.wav", 1)
			# truyen thong so chay chuong trinh  va hien thi anh len khung giao dien
			img, per, rep = bc.run(600, 450, func)
			image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()

			if cp == 1:

				# hien thi hinh anh len khung view label
				ui.view.setPixmap(QtGui.QPixmap.fromImage(image))
				ui.lcdNumber.display(rep)

				# hien thi dem thoi gian
				ui.timeLabel.setText("00:" + str(int(tt.giay / 10)) + str(int(tt.giay % 10)))

				if func < 2:
					hienhinh("balber_curl_down.jpg", "balber_curl_up.jpg", per)
				elif func == 2:
					hienhinh("bung_down.jpg", "bung_up.jpg", per)
				elif func == 3:
					hienhinh("squat_up.jpg", "squat_down.jpg", per)
				elif func == 4:
					hienhinh("push_up.jpg", "push_down.jpg", per)


		# chuc nang FORM ANALYST
		elif cp == 2:
			img, per, rep = ds.run(600, 450)  # chay ham run trong dumbbell shoulder press
			image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
			if cp == 2:
				# hien thi thoi gian
				ui.timeLabel.setText('00:' + str(int(tt.giay / 10)) + str(int(tt.giay % 10)))

				# hien thi hinh anh len khung view label
				ui.view.setPixmap(QtGui.QPixmap.fromImage(image))
				ui.lcdNumber.display(rep)
				hienhinh("dumbbell_down.jpg", "dumbbell_up.jpg", per)

		# chuc nang YOGA trong ANALYST
		elif cp == 3:
			img, check, dem, yoga_hinh = yoga.run(600, 450, 30)  # z la thoi gian uoc luong
			image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
			if cp == 3:
				# hien thi hinh anh len khung view label
				ui.view.setPixmap(QtGui.QPixmap.fromImage(image))
				ui.information_2.setVisible(check)  # hien thi hinh "dau tich xanh" khi dung
				ui.timeLabel.setText("00:" + str(int(dem / 10)) + str(dem % 10))

				if yoga_hinh == 1:
					image_path = "yoga\\1.jpg"  # path to your image file
					image_profile = QtGui.QImage(image_path)  # QImage object
					image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
														 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
					ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))
				elif yoga_hinh == 2:
					image_path = "yoga\\2.jpg"  # path to your image file
					image_profile = QtGui.QImage(image_path)  # QImage object
					image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
														 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
					ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))
				elif yoga_hinh == 3:
					image_path = "yoga\\5.jpg"  # path to your image file
					image_profile = QtGui.QImage(image_path)  # QImage object
					image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
														 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
					ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))

				#AM THANH KHI HOAN THANH
				elif yoga_hinh == 4:
					image_path = "yoga\\finish_yoga.jpg"  # path to your image file
					image_profile = QtGui.QImage(image_path)  # QImage object
					image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
														 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
					ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))


					if check2 == True:
						playS("sound\\hoanthanh.wav",0)
						playS("sound\\task_beat.wav", 1)
						check2 = False
				# ui.lcdNumber.display(rep)
				# hienhinh("dumbbell_down.jpg", "dumbbell_up.jpg", per)

		# cardio
		elif cp == 4:
			img = yoga.cardio(600, 450)  # z la thoi gian uoc luong
			image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
			if cp == 4:
				# hien thi hinh anh len khung view label
				ui.view.setPixmap(QtGui.QPixmap.fromImage(image))
				if (tt.phut < 2):  # khong che 2 bai tap trong cardio
					hienhinh_cardio("H" + str(tt.phut + 1) + ".png", "breaktime.png", tt.giay, 40)
					# ui.information_2.setVisible(check)  # hien thi hinh "dau tich xanh" khi dung
					ui.timeLabel.setText(str(int(tt.phut / 10)) + str(tt.phut % 10) + ":" +
										 str(int(tt.giay / 10)) + str(tt.giay % 10))

					if (tt.phut < 1 and tt.giay >= 55 and check2 == True):
						#print("chuongggg")
						playS1("sound\\readygo.mp3")
						check2 = False

				# dung cardio

				elif (tt.phut == 2 and phut_tt == False):
					rep += 1
					phut_tt = True
					ui.timeLabel.setText(str(int(tt.phut / 10)) + str(tt.phut % 10) + ":" +
										 str(int(tt.giay / 10)) + str(tt.giay % 10))

					playS("sound\\task_beat.wav", 1)
					playS1("sound\\hoanthanh.mp3")
					ui.view.setStyleSheet("background-color: rgb(157, 157, 157);")
					ui.view.setText(" ")
					ui.information.setStyleSheet("background-color: rgb(157, 157, 157);")
					ui.information.setText(" ")
					ui.lcdNumber.display(rep)


# AM THANH
def h_playS(a, b):  # b la cho phep chay vong lap    #0 la 1 lan, 1 la nhieu lan
	# AM THANH
	# playsound.playsound(a)
	winsound.PlaySound(a, winsound.SND_LOOP + (winsound.SND_ASYNC & b))


def playS(a, b):
	s = threading.Thread(target=h_playS, args=(a, b))
	s.start()


def h_playS1(a):  # b la cho phep chay vong lap    #0 la 1 lan, 1 la nhieu la
	# AM THANH
	playsound.playsound(a)


def playS1(a):
	s = threading.Thread(target=h_playS1, args=(a,))
	s.start()


mainUi()
t = threading.Thread(target=main)
t.start()

sys.exit(app.exec_())
