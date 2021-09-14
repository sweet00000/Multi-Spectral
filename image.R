setwd("C:/Users/Sweet/Desktop/TOMATOE/assets")

library(imager)
library(ggplot2)
library(dplyr)

img <- load.image("image.bmp")

hsv <- RGBtoHSV(img)

h <- channel(hsv, 1)

d <- as.data.frame(h)


p <- ggplot(d, aes(value))+geom_freqpoly(bins = 100)
p





#############
n=358
#############
  
l<-pull(d, value)

for (n in 360){ 
  
  n1 <- n+1
  
  for (N in 202272){ 
    
    if (l[N] < n & l[N] > n1){
      
      l[N] = 0
    
    }

  }
  
}




  

sort(l, decreasing = T)

#m <- as.cimg(m, v.name = "value")




