import cv2
import numpy as np

img1 = cv2.imread('porco_1.png')
img2 = cv2.imread('porco_2.jpeg')


dif = cv2.subtract(img1,img2)
b, g, r = cv2.split(dif)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) and cv2.countNonZero(r) == 0:
    print('Imagens tem o mesmo OBJETO')
else:
    print('As Imagens não tem o mesmo OBJETO')
    
img1 = cv2.resize(img1, (1000,650))
img2 = cv2.resize(img2, (1000,650))

cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.imshow("dif",dif)


cv2.waitKey(0)
cv2.destroyALLWindows()