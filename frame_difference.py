import cv2
import awscam

ret, current_frame = awscam.getLastFrame()
current_frame = cv2.resize(current_frame, (640,320))
previous_frame = current_frame
while True:
    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)    

    frame_diff = cv2.absdiff(current_frame_gray,previous_frame_gray)

    cv2.imshow('frame diff ',frame_diff)      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    previous_frame = current_frame.copy()
    ret, current_frame = awscam.getLastFrame()
    current_frame = cv2.resize(current_frame, (640,320))      

cv2.destroyAllWindows()
