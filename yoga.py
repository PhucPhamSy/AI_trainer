import  cv2, os
import time
import practies as pr
import numpy as np
import texttime as tt
from datetime import datetime



detector = pr.poseDetector()
giayquakhu =0
dem =  0
z =1    # chon dong tac yoga 1
check = False   #kiem tra dong tac yoga dung/sai
cap = ''
def init(a):
    global cap, detector
    if (a):
        print("bat cam")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    else:
        print("tat cam")
        cap = ''

#print (img.shape)  # h, w, c

def dem_thoigian(time):
    global giayquakhu, dem,z
    # dd/mm/YY H:M:S
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    giayhientai = tt.giay
    if giayhientai != giayquakhu:
        giayquakhu = giayhientai
        dem = dem + 1
        if dem == time+1:   # khi dem = so giay quy dinh .khong che cac tu the yoga
            dem =0          # giay tra ve 0
            z +=1           # tang thu tu dong tac lenh
            if z==5:        #
                z=1
    return dem, z

def run(x,y,time):
    global detector, cap, overlayList,z,dem, check
    success, image = cap.read()
    image = cv2.flip(image, 2)
    image = cv2.resize(image, (1280, 720))
    image = detector.findPose(image,False)
    lmList =detector.findPosition(image,False)
    if len(lmList) !=0:
        arm_r = detector.findAngle(image, 12, 14, 16)
        arm_l = detector.findAngle(image, 11, 13, 15)
        upbody_r = detector.findAngle(image, 24, 12, 14)
        upbody_l = detector.findAngle(image, 23, 11, 13)
        knee_r = detector.findAngle(image, 24, 26, 28)
        knee_l = detector.findAngle(image, 23, 25, 27)
        hip_r = detector.findAngle(image, 12, 24, 26)


        # tu the chien binh
        if z==1:
            per_arm_r = np.interp(arm_r, (175, 185), (0, 100))
            per_arm_l = np.interp(arm_l, (177, 180), (0, 100))
            per_upbody_r = np.interp(upbody_r, (90, 105), (0, 100))
            per_upbody_l = np.interp(upbody_l, (270, 280), (100, 0))
            per_knee_r = np.interp(knee_r, (125, 125), (100, 0))
            per_knee_l = np.interp(knee_l, (170, 182), (0, 100))

            # if (per_arm_r > 20 and per_arm_l > 20 and per_upbody_r > 20 and per_upbody_l > 20 and
            #         per_knee_r > 20 and per_knee_l > 20):
            #     #dem time
            #     print("qua1")
            #     check = True
            #     time_hen, z = dem_thoigian(time)

            #CHE DO NHA PHAT TRIEN TT
            if (per_arm_r>20):
                check = True
                time_hen, z = dem_thoigian(time)

            else:
                dem = 0
                check = False
        #tree
        elif (z == 2):
            per_arm_r = np.interp(arm_r, (25, 80), (100, 0))
            per_arm_l = np.interp(arm_l, (200, 325), (0, 100))
            per_upbody_r = np.interp(upbody_r, (45, 70), (100, 0))  # vai phai
            per_upbody_l = np.interp(upbody_l, (309, 290), (0, 100))
            per_knee_r = np.interp(knee_r, (30, 68), (100, 0))
            per_knee_l = np.interp(knee_l, (170, 190), (0, 100))
            per_hip_r = np.interp(hip_r, (250, 260), (0, 100))
            if (per_arm_r > 20 and per_arm_l > 20 and per_upbody_r > 20 and per_upbody_l > 20 and
                    per_knee_r > 20 and per_knee_l > 20 and per_hip_r > 10):
                print("qua2")
                check = True
                time_hen, z = dem_thoigian(time)

            else:
                dem = 0
                check = False
         #tamgiac
        elif (z == 3):
            per_arm_r = np.interp(arm_r, (184, 194), (0, 100))
            per_arm_l = np.interp(arm_l, (154, 178), (100, 0))
            per_upbody_r = np.interp(upbody_r, (80, 94), (0, 100))  # vai phai
            per_upbody_l = np.interp(upbody_l, (274, 300), (100, 0))
            per_knee_r = np.interp(knee_r, (160, 178), (0, 100))
            per_knee_l = np.interp(knee_l, (180, 190), (0, 100))
            per_hip_r = np.interp(hip_r, (136, 186), (100, 0))
            if (per_arm_r > 20 and per_arm_l > 20 and per_upbody_r > 20 and per_upbody_l > 20 and
                    per_knee_r > 20 and per_knee_l > 20 and per_hip_r > 10):
                print("qua3")
                check = True
                time_hen, z = dem_thoigian(time)
            else:
                dem = 0
                check = False

        elif (z == 4):
            cv2.rectangle(image, (10, 450), (650, 650), (170, 232, 238), cv2.FILLED)
            cv2.putText(image, f"HOAN THANH" , (20, 600),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 15)


    image = cv2.resize(image, (x, y))
    return image, check, dem, z

def cardio(x, y):
    global cap
    success, img = cap.read()
    img = cv2.flip(img, 2)
    #img1 = cv2.resize(img1, (1280, 720))
    img = cv2.resize(img, (x, y))
    return img
