from absl import app, flags, logging
from absl.flags import FLAGS
import numpy as np
import cv2


flags.DEFINE_string('video', './data/video/cars.mp4', 'path to input video or set to 0 for webcam')
flags.DEFINE_string('lane_config', './data/video/test.csv', 'path to the lanes coordinate points file')




#img = cv2.imread(r'C:\Users\khoa\Desktop\github files\yolov4-deepsort-master\data\video\test.jpg')

def main(_argv):
    try:
        vid = cv2.VideoCapture(int(FLAGS.video))
    except:
        vid = cv2.VideoCapture(FLAGS.video)
    _,img=vid.read()
    mouse_coor = []
    cv2.namedWindow("img")
    def draw_circle(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img,(x,y),10,(255,0,0),5)
            mouse_coor.append((x,y)) 

    cv2.setMouseCallback("img", draw_circle)


    while True:
    # both windows are displaying the same img
        cv2.imshow("img", img)
        k = cv2.waitKey(20) & 0xFF
    
        if k==27:
            print(mouse_coor)
            break
        if k== ord('a'):
            array=np.asarray(mouse_coor)
            with open(FLAGS.lane_config,'w') as f:     
                for a in array:
                    print(f.closed)
                    f.write("%i,%i\n" %(a[0],a[1]))
            print(mouse_coor)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
