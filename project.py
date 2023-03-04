import cv2
import os

vid=cv2.VideoCapture("Video Frame\data 2.mp4")

i=0
os.makedirs('data')

while(vid.isOpened()):
    flag,frame=vid.read()
    if flag==False:
        break
    cv2.imwrite('./data/demo'+str(i)+'.jpg',frame)
    i+=1

vid.release()
cv2.destroyAllWindows()