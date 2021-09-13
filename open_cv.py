import cv2
import numpy
import os

img = cv2.imread("assets/test.jpg", 1)

#img = cv2.resize(img, (0,0), fx=.25, fy=.25)  

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

for n in range(0, 360):

    #lower = numpy.array([0,0,0])
    #upper = numpy.array([n,255,255])   

    n1=n+1

    mask = cv2.inRange(hsv, (0,0,0), (n1,255,255))
    
    res = cv2.bitwise_and(img,img, mask= mask)

    os.chdir("C:/Users/Sweet/source/repos/open-cv/open-cv/assets/Spectral")

    cv2.imwrite(str(n)+"NM.jpg", res)



    numpy.array([0,0,0])

cv2.destroyAllWindows()


#img = cv2.resize(img, (0,0), fx=.25, fy=.25)

