setwd("C:/Users/Sweet/Desktop/TOMATOE/assets")        #set working directory

library(imager)                                       #load imager
library(ggplot2)                                      #load ggplot
library(dplyr)                                        #load dplyr

img <- load.image("image.bmp")                        #from wd load image

hsv <- RGBtoHSV(img)                                  #convert image from RGB to HSV

h <- channel(hsv, 1)                                  #keep only the hue channel form the three channel image

d <- as.data.frame(h)                                 #turn the pixel values into a data frame to work with them

p <- ggplot(d, aes(value))+geom_freqpoly(bins = 100)  #plot the frequency domain of the hue values in the image
p




                              #work in progress#

#############
n=358
#############
  
l<-pull(d, value)

for (n in 360){ 
  
  n1 <- n+1
  
  for (N in x){ 
    
    if (l[N] < n & l[N] > n1){
      
      l[N] = 0
    
    }

  }
  
}

sort(l, decreasing = T)

#m <- as.cimg(m, v.name = "value")
