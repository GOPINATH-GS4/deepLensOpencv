import numpy as np
import cv2
import awscam

cars_cascade = cv2.CascadeClassifier('./data/cars.xml')


while True:
    ret, frame = awscam.getLastFrame()
    frame = cv2.resize(frame, (640, 320))
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cars = cars_cascade.detectMultiScale(gray, 1.3, 5)
    print(cars)
    for (x,y,w,h) in cars:
        print('Cars detected ')
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('Original frame',frame)
    if cv2.waitKey(100)  != -1:
        break;
cv2.destroyAllWindows()
