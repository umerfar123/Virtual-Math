import cv2
import mediapipe as mp
import time
import math
import numpy as np

class handDetector():
    def __init__(self, mode=False, maxHands=1, model_complexity = 1, detectionCon=0.7, trackCon=0.5):
        
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity=model_complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.tip_ids=[4, 8, 12, 16, 20 ]

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity,
        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=False):
        
        lmList = []
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
        
    def fingersUp(self,landList):
        fingers=[]
    
        #for thumb up checking
        if landList[self.tip_ids[0]][2] > landList[self.tip_ids[0]-1][2]:
            fingers.append(1)
        else:
            fingers.append(0)
        #for remaining fingers up checking
        for i in range(1,5):
            if landList[self.tip_ids[i]][2] < landList[self.tip_ids[i]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
                 
def main():
    pass

if __name__ == "__main__":
    main()