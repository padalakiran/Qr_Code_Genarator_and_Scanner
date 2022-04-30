import cv2
import numpy as np
from pyzbar.pyzbar import decode


wCam, hCam =640,480

#img=cv2.imread('1.jpg')
#code=decode(img)

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

with open('Data/data.txt') as f:
    myDataList = f.read().splitlines()
#print(myDataList)
    

while True:
    success,img = cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        myData= barcode.data.decode('utf-8')
        #print(myData)

        if myData in myDataList:
            myOutput= 'Aurthorized'
            myColor = (0,255,0)
            TextColor = (0,255,0)
          #  cv2.destroyWindow(img)

        else:
            myOutput='Un-Aurthorized'
            myColor =(0,0,255)
            TextColor = (0,0,255)





        pts = np.array([barcode.polygon],np.int32)
        pts =pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1],), cv2.FONT_HERSHEY_TRIPLEX,0.9,TextColor),2        
        

        #print(code)
    if cv2.waitKey(10)==ord('q'):
        break
    cv2.imshow('result',img)
    cv2.waitKey(1)