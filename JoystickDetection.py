import dlib
import cv2
import numpy as np
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

vc = cv2.VideoCapture(0)

detector = dlib.simple_object_detector("/home/rahul/Documents/wirelessJoystick/svm/cup.svm")

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False


while rval:


    rval, frame = vc.read()
    (h,w)  = frame.shape[0:2]
    output = frame.copy()
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    rects = detector(frame)
    if len(rects) > 0:
        for k, d in enumerate(rects):
            cv2.rectangle(output, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255))
            center = (int((d.left()+d.right())/2),int((d.top()+d.bottom())/2))
            cv2.circle(output,center,1,(0,255,255),-1)
            if center[0]>w/2+20:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(output, 'Right', (0, 50), font, 1, (200, 255, 155), 2, cv2.LINE_AA)
                ser.write('2')

            elif center[0]<w/2-20:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(output, 'Left', (0, 50), font, 1, (200, 255, 155), 2, cv2.LINE_AA)
                ser.write('1')
            else:
                ser.write('0')
    else:
        ser.write('3')
    cv2.imshow("preview", output)




    key = cv2.waitKey(5) & 0xFF
    if key == 27:  # exit on ESC
        break
vc.release()
cv2.destroyAllWindows()





