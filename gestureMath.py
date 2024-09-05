import cv2
import handtracking as ht
import numpy  as np

hand = ht.handDetector()
cap = cv2.VideoCapture(0)

def handdet(frame):
    
    fingers = []
    frame = hand.findHands(frame)
    lmList = hand.findPosition(frame)
    
    if len(lmList)!=0 :
        fingers = hand.fingersUp(lmList)
        print(fingers)
        
    return frame,fingers,lmList

def draw(canvas,fingers,lmList,oldpoint):
   
    currentpoint = lmList[8][1:]
    
    if fingers == [0,1,0,0,0]:
        if oldpoint == None:
            oldpoint = currentpoint
        
        cv2.line(canvas,pt1=oldpoint,pt2=currentpoint,color=(0,255,255),thickness=10)
        oldpoint = currentpoint
        
    elif fingers == [0,0,0,0,0]:
        
        canvas = np.zeros_like(frame)
              
    return canvas
def senttoAi(frame):
    

oldpoint= None
canvas = None
currentpoint = None

while True:
    
    status, frame = cap.read()
    
    if not (status):
        print("Capturing error")
        
    if canvas is None:
        canvas = np.zeros_like(frame)
    
    frame = cv2.resize(frame, (720,400))
    frame = cv2.flip(frame , 1)
    
    frame,fingers,lmList = handdet(frame)
    
    if len(lmList)!=0:
        
        canvas = draw(canvas,fingers,lmList,oldpoint)
    
   
        
    
    cv2.imshow('Gesture Math',frame)
    cv2.imshow('canvas',canvas)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cv2.destroyAllWindows()
cap.release()
        