"""
Hand Tracing Module
By: Niare Doyom
"""
import cv2
import mediapipe as mp
import time
class handDetector():

    # the first function is just an initialization function, it initializes some values to make it usable in other
    # methods or functions
    # the class hand detector itself consists of several argument
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        # hands can be essentially used as a function to get the results
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        # mpDraw can essentially be used as a function to Draw the hands
        self.mpDraw = mp.solutions.drawing_utils

    # the first function defined for the class Hand detectors, main purpose is to return image with hands drawn on it
    def findHands(self, img, draw=True):  # two arguments which image you want to use and want to draw hands?
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converts BGR to RGB
        self.results = self.hands.process(imgRGB)  # list of two values. one all required values for hand 0
        # print(results.multi_hand_landmarks)                           # second all required values for hand 1
        if self.results.multi_hand_landmarks:      # result will either be none or that list that we talked about
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  # draws lines and connection by taking the data handLms and image img
        return img

    # this function returns a list of which each element is a list which contains id, x coord and y coord of a landmark point in hand

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []  # each element is a list which contains id, x coord and y coord of a landmark point in hand
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList


def main():
    pTime = 0  # previous time
    cTime = 0  # current time
    cap = cv2.VideoCapture(0)  # tells programme from which camera you should start capturing video
    detector = handDetector()  # Class Hand detector as defined above
    while True:
        success, img = cap.read()
        img = detector.findHands(img)  # resets img so that there are landmarks drawn on img and also draws the lines on img
        lmList = detector.findPosition(img)  # returns a list of elements containing a list of id, x coord and y coord of each hands, also draws the circles on img
        if len(lmList) != 0:  # if there are no hands on screen it will be a null list
            print(lmList[0])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":  # if the module is called then run main()
    main()