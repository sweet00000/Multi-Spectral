import cv2                                          #import computer vision
import os                                           #import os

img = cv2.imread("assets/test.jpg", 1)              #read the image

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)          #convert the RGB image to HSV

for n in range(0, 360):                             #loop for every number between 0 and 360(roughly the visible spectrum)

    n1=n+1                                          #add one to n and make it a new variable n1(used to threshold values)

    mask = cv2.inRange(hsv, (n,0,0), (n1,255,255))  #mask hue values outside the range n to n1, make this the mask
    
    res = cv2.bitwise_and(img,img, mask= mask)      #lay the mask over the original image
    
    os.chdir("C:/Users/Sweet/Spectral")             #set the working directory to a new folder

    cv2.imwrite(str(n)+"NM.jpg", res)               #save the new masked image in the folder as its hue value specified by the for loop

cv2.destroyAllWindows()                             #close everything
