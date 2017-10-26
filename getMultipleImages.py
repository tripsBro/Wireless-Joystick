import cv2
import numpy as np

vc = cv2.VideoCapture(0)


if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

count = 0
number = 0
while rval:


    rval, frame = vc.read()

    #--count, wait and save --
    count += 1

    if count % 40 == 0:
        number +=1

        cv2.imwrite("./testingImages/frame%d.jpg" % number, frame)
        print "no. of images written: %d"%(number)

    cv2.imshow("preview", frame)




    key = cv2.waitKey(5) & 0xFF
    if key == 27:  # exit on ESC
        break
vc.release()
cv2.destroyAllWindows()
