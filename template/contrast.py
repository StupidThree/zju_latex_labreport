import cv2
import os
import numpy as np

files=os.listdir("pic")

for pic_name in files:
    I=cv2.imread("pic/"+pic_name,cv2.IMREAD_GRAYSCALE)
    Imax,Imin=np.max(I),np.min(I)
    Omax,Omin=255,0
    a=float(Omax-Omin)/(Imax-Imin)
    b=Omin-a*Imin
    O=a*I+b
    O=O.astype(np.uint8)
    cv2.imwrite("pic/"+pic_name,O)
