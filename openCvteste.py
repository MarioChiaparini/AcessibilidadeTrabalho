from curses import start_color
from symbol import star_expr
from tracemalloc import start
import cv2
from cv2 import COLOR_RGB2BGR
from matplotlib import pyplot as plt 
import easyocr_code as easy 
import easyocr

#vid = cv2.VideoCapture(0)
'''  
while(True):
      
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    #mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    #im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    #biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    #x,y,w,h = cv2.boundingRect(biggest_contour)
    start_point = (50,50)
    end_point = (220,220)
    color = (255,0,0)
    thickness = 2 
    image = cv2.rectangle(vid, start_point, end_point, color, thickness)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()

cv2.destroyAllWindows()
'''


def on_mouse(event,x,y,flags,params):

    global rect,startPoint,endPoint, selected_ROI

    if event == cv2.EVENT_LBUTTONDOWN:

        if startPoint == True and endPoint == True:
            startPoint = False
            endPoint = False
            rect = (0, 0, 0, 0)
            selected_ROI = False

        if startPoint == False:
            rect = (x, y, 0, 0)
            startPoint = True

        elif endPoint == False:
            rect = (rect[0], rect[1], x, y)
            endPoint = True
            selected_ROI = True

video = cv2.VideoCapture(0)
rect = [50,50,320,320]
while video.isOpened():
    ret, frame = video.read()
    cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (255, 0, 255), 2)
    region = frame[rect[0]:rect[1], rect[2]:rect[3]]
    cv2.imshow('original', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
easy.overlay_ocr_text(region)
video.release()
cv2.destroyAllWindows()