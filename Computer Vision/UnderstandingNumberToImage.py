#Generating colors from numbers!
#Understanding the ROOT, All images are just numbers to computer
#That's how they process it
#Shows BLUE ,GREEN ,RED IMAGES
import cv2
print(cv2.__version__)

import numpy as np
while True:
    frame = np.zeros([300,300,3],dtype=np.uint8)
    frame[:,:] = [0,0,255]
    frame[:,:100] = [255,0,0]
    frame[:,100:200] = [0,255,0]
    cv2.imshow('MYWINDOW',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break



