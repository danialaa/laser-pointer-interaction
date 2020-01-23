import numpy as np
import cv2
import time
import image
import winsound
from shapedetector import ShapeDetector
import imutils



frequency = 1500
duration = 100
cap = cv2.VideoCapture(0)
i=0
xarray=[0]
yarray=[0]
while(True):
    # Capture frame-by-frame
    start_time = time.time()
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    (minval,maxval,minloc,maxloc) = cv2.minMaxLoc(gray)
    cv2.circle(gray, maxloc,21,(255,0,0),2)
    # Display the resulting frame
   
    
    
    time.sleep(0.2) 
    orig= frame.copy();
    
    
    cv2.imshow("", gray)
    (x,y) = maxloc
    print(x)
    print(y)
    if(i==0):
        xarray=[x]
        yarray=[y]
    if(i>0):
        if(abs(x-xarray[-1])>20 or abs(y-yarray[-1])>20):
            if(i==1):
                del xarray[-1]
                del yarray[-1]
            xarray.append(x)
            yarray.append(y)
            print("added")
            
        else:
            if(len(xarray)>6):
                del xarray[-1]
                del yarray[-1]
                blank_image= np.zeros(shape=[640,480,3],dtype=np.uint8)
                blank_image.fill(255)
                for x in range(len(xarray)):
                    thick=2
                    cv2.line(blank_image,(xarray[x-1],yarray[x-1]),(xarray[x],yarray[x]),(255,0,0),4)
                   
                
                
                winsound.Beep(frequency,duration)
                break;
                 
            xarray.clear()
            yarray.clear()
            i=-1
            print("cleared")
            
            

    i=i+1

    
            
        
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Sleep for 1 second minus elapsed time
    


# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

# loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]))
	cY = int((M["m01"] / M["m00"]))
	shape = sd.detect(c)

	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	c = c.astype("int")
	cv2.drawContours(blank_image, [c], -1, (0, 255, 0), 2)
	cv2.putText(blank_image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)

	# show the output image
	cv2.imshow("Image", blank_image)
	cv2.waitKey(0)
# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
