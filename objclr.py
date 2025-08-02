import cv2
import imutils

cam=cv2.VideoCapture(0)

redLower=(86,53,64)
redUpper=(174,192,255)

while True:
    (grabbed,frame)=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frames=imutils.resize(frame,width=1000)
    blur=cv2.GaussianBlur(hsv,(11,11),0)

    mask=cv2.inRange(hsv,redLower,redUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)

    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts)>0:
     c=max(cnts,key=cv2.contourArea)
     ((x,y),radius)=cv2.minEnclosingCircle(c)
    M=cv2.moments(c)
    if["m00"]!=0:
           center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
    else:
           center=(0,0)

    if radius>0:
           cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,0),2)
           cv2.circle(frame,center,5,(0,0,255),-1)
           
    cv2.imshow("tracker",frame)
    key=cv2.waitKey(1000)
    if key==27:
     print(key)
     break
cam.release()
cv2.destroyAllWindows()


            
               
           

           

       
    
    


    

    
        
    
    
    
    





