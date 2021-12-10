import cv2
import mediapipe as mp
import time


class FaceDetector():
    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils  # can be used as a function to draw lm on an image
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)  # can be used to get the landmarks on face

    def findFaces(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)

        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box  # a user created data type consisting x coord, y coord, height and the width of bounding box of the face with id = id in ratios
                ih, iw, ic = img.shape  # gets the size of the screen

                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)  #  a tuple consisting x coord, y coord, height and the width of bounding box of the face with id = id in pixels

                bboxs.append([id, bbox, detection.score])

                if draw:
                    img = self.fancyDraw(img, bbox)
                    cv2.putText(img, str(int(detection.score[0] * 100)) + '%', (bbox[0], bbox[1] - 20),
                                cv2.FONT_HERSHEY_TRIPLEX, 0.6, (233, 0, 0), 1)
                #cv2.rectangle(img, bbox, (255,0,255), 1)

        return img, bboxs

    def fancyDraw(self, img, bbox, l=10, t=3, rt=1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        cv2.rectangle(img, bbox, (255, 0, 255), rt)
        # Top left, x, y
        cv2.line(img, (x,y),(x+l, y), (255, 0, 255), t)
        cv2.line(img, (x, y), (x, y + l), (255, 0, 255), t)

        # Top right, x1, y
        cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y + l), (255, 0, 255), t)

        # bottom left, x, y
        cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)

        # bottom left, x, y
        cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)

        return img

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, "FPS " + str(int(fps)), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (233, 0, 0), 1)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        print(bboxs)


if __name__ == "__main__":
    main()