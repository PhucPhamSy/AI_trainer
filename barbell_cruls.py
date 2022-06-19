import cv2, time
import numpy as np
from practies import poseDetector


cap = ''
detector = poseDetector()
count = 0
rep_up = 0
pTime = 0
per = 0

def init(a):
    global cap, detector, count
    if (a):
        print("bat cam")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    else:
        print("tat cam")
        cap = ''   # giai phong cap.realease
        count = 0


def run(x, y, z):   #x, y la resize kichs thuoc     z: quy dinh cac chuc nang chuong trinh
    global count, rep_up, pTime, detector,cap, per
    #print("chay run")

    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = cv2.flip(img, 2)
    img = detector.findPose(img, draw=False)
    lmList= detector.findPosition(img, draw=False)
    if len(lmList)!=0:
        if z==1:
            #right arm
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle,(220,300),(0,100))
            bar = np.interp(angle,(220,300),(650,100))
        elif z==0:
            # left arm
            angle = detector.findAngle(img, 12, 14, 16)
            per = np.interp(angle, (30, 120), (100, 0))
            bar = np.interp(angle, (30, 120), (100, 650))
        elif z==2:
            #abs
            # print("chay abs")
            angle = detector.findAngle(img, 11, 23, 25)
            per = np.interp(angle, (190, 240), (0, 100))
            bar = np.interp(angle, (190, 240), (650, 100))
        elif z==3:
            # squat
            angle = detector.findAngle(img,24,26,28)
            per = np.interp(angle,(190,260),(0,100))
            bar = np.interp(angle,(190,260),(650,100))
        elif z == 4:
            # pushup
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (200, 280), (0, 100))
            bar = np.interp(angle, (200, 300), (650, 100))

        #check for rep
        color = (255,0,255)
        if per == 100:
            color = (255,0,255)
            if rep_up==0:
                count+=0.5
                rep_up =1
        if per == 0:
            color = (0, 255, 0)
            if rep_up == 1:
                count+=0.5
                rep_up = 0
        #print (count)
#ve bar
        cv2.rectangle(img, (1100,100),(1175,650),(255,255,255),3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), (255,0,255), cv2.FILLED)
        cv2.putText(img,f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 3)

    img = cv2.resize(img, (x, y))

    return img, per, count



