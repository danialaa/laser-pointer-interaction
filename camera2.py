import numpy as np
import cv2
import time
import image
import winsound
from pynput.keyboard import Key, Controller

keyboard = Controller()
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
                    cv2.line(blank_image,(xarray[x-1],yarray[x-1]),(xarray[x],yarray[x]),(0,255,0),2)
                   
                
                
                winsound.Beep(frequency,duration)
                break;
                 
            xarray.clear()
            yarray.clear()
            i=-1
            print("cleared")
            
            

    i=i+1

    
            
        
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
    
cv2.imshow("", blank_image)
#gesturecheck
#if(gesture=="square"):
   # keyboard.press(Key.left)
#elif gesture=="circle":
   # keyboard.press(Key.right)

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
