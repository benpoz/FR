import cv2
import numpy as np
import serial

x_center = 255
y_center = 165
arduino_x = serial.Serial('com8',9600) 
arduino_z = serial.Serial('com7',9600) 

video_capture = cv2.VideoCapture(1)
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def move_x(avg_x):
    if avg_x > x_center+50:
        arduino_x.write(b'r')
        print('right')
    elif avg_x < x_center-50 and not avg_x ==0:
        arduino_x.write(b'l')
        print('left')
    else:
        arduino_x.write(b's')
        print('stop')

def move_z(avg_y):
    if avg_y > y_center+100 and not avg_y == 0:
        arduino_z.write(b'u')
        print("up")
    elif avg_y < y_center-100:
        arduino_z.write(b'd')
        print('down')
    else:
        arduino_z.write(b's')
        print('stop')
        
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))

    avg_x = 0
    avg_y = 0
    
    for (x, y, w, h) in faces:
        avg_x += x + w//2
        avg_y += y + h//2
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 0, 255), 4)
    
    if faces == ():
        faces = np.zeros(shape=(1,1))
        
    avg_y = avg_y // faces.shape[0]
    avg_x = avg_x // faces.shape[0]

    move_x(avg_x)
    move_z(avg_y)
    
    return faces

while True:

    result, video_frame = video_capture.read()  
    if result is False:
        break  

    faces = detect_bounding_box(video_frame) 

    cv2.imshow("My Face Detection Project", video_frame) 

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()