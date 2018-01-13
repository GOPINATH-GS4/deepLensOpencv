import cv2
import awscam

ret, frame = awscam.getLastFrame()

cv2.imshow("Frame", frame)

cv2.waitKey(0)

cv2.destroyAllWindows()
