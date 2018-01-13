# DeepLens Opencv samples 

### This repository contains examples on how to access camera in DeepLens and run OpenCV using the frame grabbed from the camera 


### Device Library 

To capture the camera feed from the DeepLens we use the device Library provided by Amazon, the camera comes with all the libraries, so no need to install anything new. For the documentation on the device library please refer to [Device Library](https://docs.aws.amazon.com/deeplens/latest/dg/deeplens-device-library.html)

The key method is ````awscam.getLastFrame()````

````hello_world.py````

````
import cv2
import awscam

ret, frame = awscam.getLastFrame()

cv2.imshow("Frame", frame)

cv2.waitKey(0)

cv2.destroyAllWindows()

````

if there is any application running in DeepLens deployed through AWS it needs to be stopped first, if not you willnot get good frames and it library will error out 

## Stop the service 

````
sudo service greengrassd stop  

````

# Running the samples 

if you are logged in through remopte ssh make sure you are logged in with -X or -Y (trusted) options 

```` example : ssh -Y aws_cam@192.168.1.244 ```` 

The userid of deepLens is aws_cam and the ip-address can be obtained by looking through your router, the default hostname will be ````Deepcam```` 


````
git clone https://github.com/GOPINATH-GS4/deepLensOpencv.git

cd deepLensOpencv

sudo service greengrassd stop  

python hello_world.py 

python video_display.py 
 
python face_detection.py 

python cars_detection.py 
 
````

