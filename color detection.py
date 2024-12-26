import cv2
import numpy as np
from numpy import pi
kamera = cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1360)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True :
    _, frame = kamera.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    
    cx = int(width/2)
    cy = int(height/2)
    
    cv2.circle(frame , (cx,cy), 5, (25,25,25), 0)
    
    pixel_center = hsv_frame[cy, cx]
    hue = pixel_center[0]
    saturation = pixel_center[1]
    value = pixel_center[2]
    
    color = "cant detect"
    if hue == 0 | saturation == 0 :
        color = "putih"
    
    print(pixel_center)
    
                         
    cv2.imshow("color detection", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    if hue == 0 | saturation == 0 :
        color = "putih"
    elif hue < 5 :
        color = "merah"
    elif hue < 10 :
        color = "coklat"
    elif hue < 17 :
        color = "oren"
    elif hue < 34 :
        color = "kuning"
    elif hue < 75 :
        color = "hijau"
    elif hue < 110 :
        color = "biru"
    elif hue < 151 :
        color = "ungu"
        
        
    pixel_center_bgr = frame[cy,cx]

    b = int(pixel_center_bgr[0])
    g = int(pixel_center_bgr[1])
    r = int(pixel_center_bgr[2])

    print(pixel_center)
    cv2.putText(frame, color, (cx - 100,cy - 150), 0, 1.5, (b, g, r), 8)
    cv2.circle(frame, (cx,cy), 5, (25, 25, 25), 0)
    
    cv2.imshow("color detection", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()







