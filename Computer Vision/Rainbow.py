#Creating a rainbow when we covert the color from HSV to BGR format

import cv2 
import numpy as np

x = np.zeros([256,720,3],dtype=np.uint8)
for row in range(0,256,1):
    for column in range(0,720,1):
        x[row,column] = (int(column/4),row,255)
x = cv2.cvtColor(x,cv2.COLOR_HSV2BGR)
while True:
    cv2.imshow('my HSV',x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()