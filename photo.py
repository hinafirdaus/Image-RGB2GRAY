import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

path=r'D:/papa1.png'
pic=cv2.imread(path,cv2.IMREAD_COLOR)
if (pic is not None):
    cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

plt.imshow(pic[:,:,::-1])

rgb_img=cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
grey_img=cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
invert_img=cv2.bitwise_not(grey_img)
blur_img=cv2.GaussianBlur(invert_img,(111,111),0)
invblur_img=cv2.bitwise_not(blur_img)
sketch_img=cv2.divide(grey_img, invblur_img, scale=256.0)
cv2.imwrite('sketch.png', sketch_img)
cv2.imshow('sketch image', sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('D:/papa_ji.png',sketch_img)
