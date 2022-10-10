import cv2 
import easyocr
import os
from numba import jit, cuda

#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   
#os.environ["CUDA_VISIBLE_DEVICES"]="0"
#from tensorflow.python.client import device_lib
#print (device_lib.list_local_devices())


cap = cv2.VideoCapture(0)
reader = easyocr.Reader(['en'], gpu=False)

while True :
    _, frame = cap.read()
    result = reader.readtext(frame)
    for detection in result:
        top_left = (int(detection[0][0][0]),int(detection[0][0][1]))
        #print(detection[0])
        #print(detection[0][0][0])
        bottom_right = (int(detection[0][2][0]),int(detection[0][2][1]))
        #print(bottom_right(0))
        text = detection[1]
        print (text)
        img = cv2.rectangle(frame,top_left,bottom_right,(0,255,0),2)
    cv2.imshow("Text Recgnition",frame)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()