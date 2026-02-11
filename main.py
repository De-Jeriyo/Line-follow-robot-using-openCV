<<<<<<< HEAD
from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule
# import cv2

##################################################
motor = Motor(2, 3, 4, 17, 22, 27)


##################################################

def main():
    img = WebcamModule.getImg()
    curveVal = getLaneCurve(img, 1)

    sen = 1.3  # SENSITIVITY
    maxVAl = 0.3  # MAX SPEED
    if curveVal > maxVAl: curveVal = maxVAl
    if curveVal < -maxVAl: curveVal = -maxVAl
    # print(curveVal)
    if curveVal > 0:
        sen = 1.7
        if curveVal < 0.05: curveVal = 0
    else:
        if curveVal > -0.08: curveVal = 0
    motor.move(0.20, -curveVal * sen, 0.05)
    # cv2.waitKey(1) #for display


if __name__ == '__main__':
    while True:
=======
from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule
# import cv2

##################################################
motor = Motor(2, 3, 4, 17, 22, 27)


##################################################

def main():
    img = WebcamModule.getImg()
    curveVal = getLaneCurve(img, 1)

    sen = 1.3  # SENSITIVITY
    maxVAl = 0.3  # MAX SPEED
    if curveVal > maxVAl: curveVal = maxVAl
    if curveVal < -maxVAl: curveVal = -maxVAl
    # print(curveVal)
    if curveVal > 0:
        sen = 1.7
        if curveVal < 0.05: curveVal = 0
    else:
        if curveVal > -0.08: curveVal = 0
    motor.move(0.20, -curveVal * sen, 0.05)
    # cv2.waitKey(1) #for display


if __name__ == '__main__':
    while True:
>>>>>>> 055e4ac1e99b6991a0e4e5d0fba9c7fe942d451e
        main()