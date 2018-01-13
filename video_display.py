import awscam
import cv2


while(True):
    ret, frame = awscam.getLastFrame()
    frame = cv2.resize(frame, (640, 320))
    cv2.imshow('frame',frame)
  
    if cv2.waitKey(100) != -1:
        break;
    
cv2.destroyAllWindows()
