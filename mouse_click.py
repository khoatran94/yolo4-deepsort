import numpy as np
import cv2


mouse_coor = []
def draw_circle(event,x,y,flags,param):
    global mouse_coor
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(255,0,0),5)
        mouse_coor.append((x,y)) 


#img = cv2.imread(r'C:\Users\khoa\Desktop\github files\yolov4-deepsort-master\data\video\test.jpg')
vid=cv2.VideoCapture(r'https://verkehrsservice.hessen.de/syncdata/video/k5370.mp4')
_,img=vid.read()
cv2.namedWindow("img")
cv2.setMouseCallback("img", draw_circle)

while True:
    # both windows are displaying the same img
    cv2.imshow("img", img)
    k = cv2.waitKey(20) & 0xFF
    
    if k==27:
        print(mouse_coor)
        break
    if k== ord('a'):
        f=open('./data/video/coordinates.csv','w')     
        array=np.asarray(mouse_coor)
        for a in array:
            f.write("%i,%i\n" %(a[0],a[1]))
        f.close()
        
        # startramya change the 
         #end of change   

cv2.destroyAllWindows()
