import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    blur = cv2.GaussianBlur(frame,(5,5),cv2.BORDER_DEFAULT) 
 
    cv2.imshow('original',frame)
    cv2.imshow('blur',blur)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()