#Creating multiple region of interst right in the middle of the screen
#Also selecting the ROI, and showing it in different window
#And Applying operations on the ROI, like converting it to gray scale

import cv2
print(cv2.__version__)

width=640
height=360

cam=cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,frame = cam.read()

    frameROI = frame[150:210,250:390]
    grayframeROI = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)

    frameROIBGR = cv2.cvtColor(grayframeROI, cv2.COLOR_GRAY2BGR)
    cv2.imshow('grayBGR',frameROIBGR)
    cv2.moveWindow('grayBGR',650,180)
    frame[150:210,250:390] = frameROIBGR
    
    cv2.imshow('grayROI',grayframeROI)
    cv2.moveWindow('grayROI',650,90)
    cv2.imshow('ROI', frameROI)
    cv2.moveWindow('ROI',650,0)
    cv2.imshow('WEBCAME',frame)
    cv2.moveWindow('WEBCAM',0,0)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()


import cv2

width = 640
height = 360
