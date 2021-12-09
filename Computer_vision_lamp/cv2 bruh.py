import serial
import time
import cv2
import handtrackingModule as hm
import numpy as np
import math
arduinoData = serial.Serial('COM3', 9600)


x = 0
y = 0
time.sleep(3)




pTime = 0  # previous time
cTime = 0  # current time
cap = cv2.VideoCapture(0)  # tells programme from which camera you should start capturing video
detector = hm.handDetector(maxHands=1)  # Class Hand detector as defined above
pLenlist = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)  # resets img so that there are landmarks drawn on img and also draws the lines on img
    lmList = detector.findPosition(img, draw=False)  # returns a list of elements containing a list of id, x coord and y coord of each hands, also draws the circles on img
    if len(lmList) != 0:  # if there are no hands on screen it will be a null list
        i = 9
        print(lmList[i])
        x, y = int(np.interp(lmList[i][1], [220, 420], [0, 180])), int(np.interp(lmList[i][2], [140, 340], [0, 180]))
        if math.hypot(lmList[20][1] - lmList[4][1], lmList[20][2] - lmList[4][2]) < 20:
            arduinoData.write(bytes("X" + str(x) + "Y" + str(y), 'UTF-8'))
        print(math.hypot(lmList[20][1] - lmList[4][1], lmList[20][2] - lmList[4][2]))

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    #cv2.imshow('jj', img)

    if pLenlist != 0:
        time.sleep(3)
    else:
        cv2.waitKey(10)
