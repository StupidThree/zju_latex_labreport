import cv2
import os

files=os.listdir("pic")

for pic_name in files:
    print(pic_name)
    img=cv2.imread("pic/"+pic_name,-1)
    h,w=img.shape[:2]

    t=int(min(h/3,w/4))
    size=(t*4,t*3)
    new_img=255-cv2.resize(img,size,interpolation=cv2.INTER_AREA)
    cv2.imwrite("pic/"+pic_name,new_img)
