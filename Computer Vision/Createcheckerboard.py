#Another Cool Small Demo
#Where you create a Checkerboard using simple for loop and conditionals

import cv2
import numpy as np

boardSize = int(input("What Size is your board ? "))
numSquare = int(input("And How many Squares ? "))
sqaureSize = int(boardSize / numSquare)

darkColor = (0,0,0)
lightColor = (255,255,255)
nowColor = darkColor

while True:
    x = np.zeros([boardSize,boardSize,3],dtype = np.uint8)

    for row in range(0,numSquare):
        for column in range(0,numSquare):
            x[sqaureSize*row:sqaureSize*(row+1),sqaureSize*column:sqaureSize*(column+1)] = nowColor
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor

    cv2.imshow("WEBCAM",x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
