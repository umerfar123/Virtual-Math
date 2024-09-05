import cv2
import handtracking as ht
import numpy  as np
from PIL import Image
import os
from api import apk
import streamlit as st

import google.generativeai as genai
genai.configure(api_key=apk)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

st.set_page_config(layout= 'wide')
st.image('D:\Projects\Opencv\mathgesture\GestureMath.png')
col1,col2 = st.columns([1,2])


with col2:
    st.checkbox('Run',value=True)
    col2_window = st.image([])
    
with col1:
    st.title("Answers:")
    col1_window = st.subheader(" ")
    

hand = ht.handDetector()
cap = cv2.VideoCapture(0)

def handdet(frame):
    
    fingers = []
    frame = hand.findHands(frame)
    lmList = hand.findPosition(frame)
    
    if len(lmList)!=0 :
        fingers = hand.fingersUp(lmList)
        
    return frame,fingers,lmList

def draw(canvas,fingers,lmList,oldpoint):
   
    currentpoint = lmList[8][1:]
    
    if fingers == [0,1,0,0,0]:
        if oldpoint == None:
            oldpoint = currentpoint
        
        cv2.line(canvas,pt1=oldpoint,pt2=currentpoint,color=(0,255,255),thickness=10)
        oldpoint = currentpoint
        
    elif fingers == [1,0,0,0,0]:
        
        canvas = np.zeros_like(frame)
              
    return canvas

def senttoAi(frm,fingers):
    
    if fingers == [0,1,0,0,1]:
        PIL_image = Image.fromarray(frm)
        response = model.generate_content(["solve this math problem",PIL_image])
        return response.text
    

oldpoint= None
canvas = None
currentpoint = None
aioutput = None

while True:
    
    status, frame = cap.read()
    frame = cv2.resize(frame, (720,400))
    frame = cv2.flip(frame , 1)
    
    if not (status):
        print("Capturing error")
        
    if canvas is None:
        canvas = np.zeros_like(frame)
    
    frame,fingers,lmList = handdet(frame)
    
    if len(lmList)!=0:
        canvas = draw(canvas,fingers,lmList,oldpoint)
        aioutput = senttoAi(canvas,fingers)
        
    frame_combined = cv2.addWeighted(frame,0.7, canvas,0.3,1)
    
    col2_window.image(frame_combined, channels='BGR')
    if aioutput:
        col1_window.text(aioutput)
    #cv2.imshow('Gesture Math',frame_combined)
    #xcv2.imshow('canvas',canvas)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cv2.destroyAllWindows()
cap.release()
        