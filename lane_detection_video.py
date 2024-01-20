import cv2 as cv
import numpy as np
import time
import sys


video = cv.VideoCapture("D:/YOMTECH PROJECTS/my python/test/lane1.avi")

if not video.isOpened():
    sys.exit("unable to load video frame")

while True:
    
    __, frame = video.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
    canny = cv.Canny(frame, 255, 255, apertureSize=3)
    
    kervel = np.ones((5,5), np.uint8)
    
    close1 = cv.morphologyEx(canny, cv.MORPH_CLOSE, kervel)
    
    close = cv.morphologyEx(close1, cv.MORPH_CLOSE, kervel)
        
    line = cv.HoughLinesP(close, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    
   
    
    try:
        for lines in line:
            flag = 1
            x1,y1,x2,y2 = lines[0]

            print(lines[0])

            cv.line(frame, (x1,y1),(x2,y2), (0,255,0), 2)
            
            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(frame, "keep going", (500,500), font, 3, (0,0,255), 5)
            
    
    
    except TypeError:
            
            
            cv.putText(frame, "Oh!! i cant see", (500,500), font, 3, 255, 5)
            
            continue
                
    
    cv.imshow("my video", frame)
    
    cv.imshow("canny", close)
    
  
    
    
    key = cv.waitKey(1)
    
    if key == ord("q"):
        break
        
video.release()
cv.destroyAllWindows()
