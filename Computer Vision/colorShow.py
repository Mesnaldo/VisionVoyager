#Intersting program, where when you click at the pixels in the screen
#It shows you what color it is in (RGB) format 
#And also what color it is another window
#Pretty Cool

import cv2

print(cv2.__version__)
import numpy as np

evt = 0
xVal = 0
yVal = 0

def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global xVal
    global yVal
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt = event
        xVal = xPos
        yVal = yPos
    if event == cv2.EVENT_RBUTTONDOWN:
        print(event)
        evt = event
        xVal = xPos
        yVal = yPos


width = 620
height = 340

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore, frame = cam.read()
    if evt == 1:
        x = np.zeros([250,250,3],dtype=np.uint8)  #Look at the 3dimen format#
        clr = frame[yVal][xVal]    #Imp as it picks that xpos and yPos of colour#
        print(clr)
        x[:,:] = clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow('Color Picker',x)
        cv2.moveWindow('Color Picker',width,0)
        evt = 0
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
