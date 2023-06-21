# This Trackbars program will be able to create a circle
# And using trackbar features to control the xpos, ypos, radius and thickness of circle

import cv2
print(cv2.__version__)

def myCallBack1(val):
    global xPos
    print("xPos:",val)
    xPos = val
def myCallBack2(val):
    global yPos
    print("yPos: ",val)
    yPos = val
def myCallBack3(val):
    global myrad
    myrad = val
def myCallBack4(val):
    global thick
    thick = val


width=640
height=360

myrad = 25
thick = 1

xPos = int(width/2)
yPos = int(height/2)

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,100)
cv2.moveWindow('myTrackbars',width,0)
cv2.createTrackbar('xPos','myTrackbars',xPos,500,myCallBack1)
cv2.createTrackbar('yPos','myTrackbars',yPos,1000,myCallBack2)
cv2.createTrackbar('radius','myTrackbars',myrad,int(height/2),myCallBack3)
cv2.createTrackbar('thickness','myTrackbars',thick,7,myCallBack4)
while True:
    if thick == 0:
        thick = -1
    ignore,  frame = cam.read()
    cv2.circle(frame,(xPos,yPos),myrad,(255,0,0),thick)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
