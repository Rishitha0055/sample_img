import os
import cv2
path='/home/tgt/Desktop/center_wise/'
new_path = '/home/tgt/face_detection_results'

haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def detected_faces(img,a,b):
    gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #print(gray_img)
    faces_rect=haar_cascade.detectMultiScale(gray_img,scaleFactor=2.2)
    #print(faces_rect)
    #print(len(faces_rect))
    if  len(faces_rect) == 1:
        pass
        #print(True)
    else:
        pass
    
    for (x,y,w,h) in faces_rect:
            cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),thickness=2)
    

    
    if not os.path.exists(os.path.join(new_path,a)):
        os.mkdir(os.path.join(new_path,a))
    else:
        pass
        
    
    cv2.imwrite(os.path.join(new_path,a,b),img)

for a in os.listdir(path):
    print(a)
    """for b in os.listdir(path+a):
        if len(b) == 14:
            #print(b)
            img = cv2.imread(path+a+'/'+b ,cv2.IMREAD_UNCHANGED)
            #print(img)
            #center_code = b[0:6]
            detected_faces(img,a,b)"""
