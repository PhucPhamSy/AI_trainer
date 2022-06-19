import  cv2
import practies as pr
import numpy as np


#print (img.shape)  # h, w, c
cap = ''
detector = pr.poseDetector()
count = 0
rep_up=0
per_r = 0

def init(a):
    global cap, detector, count
    if (a):
        print("bat cam")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        #detector = poseDetector()
    else:
        print("tat cam")
        #cv2.VideoCapture(0, cv2.CAP_DSHOW).release()
        cap = ''
        count = 0

def run(x, y):
    global cap, detector, count, rep_up, per_r
    success, image = cap.read()
    image = cv2.resize(image, (1280, 720))
    image = cv2.flip(image, 2)
    #img = cv2.imread(path_img)
    #image = cv2.resize(img, (1020,954), interpolation=cv2.INTER_AREA)
    image = detector.findPose(image,False)
    lmList =detector.findPosition(image,False)
    wrist = []
    if len(lmList) !=0:
        arm_r = detector.findAngle(image, 12, 14, 16)
        arm_l = detector.findAngle(image, 11, 13, 15)
        upbody_r =detector.findAngle(image,24,12,14,False)
        upbody_l = detector.findAngle(image, 23, 11, 13,False)
        per_l = np.interp(upbody_l, (235, 270), (100, 0))
        per_r = np.interp(upbody_r, (95, 124), (0, 100))
        if lmList[11][2]>lmList[14][2]:  #  khuy tay cao hon vai
            wrist.append([lmList[14][1], lmList[14][2]-detector.lenght(image,14,16)]) # ve co tay chuan ben phai
            wrist.append([lmList[13][1], lmList[13][2]-detector.lenght(image,14,16)])#ve co tay chuan trai
            angle_r = detector.cosin2goc(image,wrist[0],14,16)
            angle_l = detector.cosin2goc(image, wrist[1], 13, 15)

        if (per_l == 100 and per_r == 100):
            color = (255,0,255)
            if rep_up==0:
                count+=0.5
                rep_up =1
        if (per_l == 0 and per_r==0):
            color = (0, 255, 0)
            if rep_up == 1:
                count+=0.5
                rep_up = 0
        #print (count)

    #print(lmList[0][2],lmList[13][2])
    # print(count)
    # cv2.rectangle(image, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
    # cv2.putText(image, str(int(count)), (40, 670), cv2.FONT_HERSHEY_PLAIN, 10,
    #             (255, 0, 0), 13)




    image = cv2.resize(image, (x, y))

    return image, per_r, count