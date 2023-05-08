import cv2
import numpy as np

x_center = 320
y_center = 230


video_capture = cv2.VideoCapture(1)
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    
    avg_x = 0
    avg_y = 0
    
    for (x, y, w, h) in faces:
        avg_x += x
        avg_y += y
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 0, 255), 4)
    
    if faces == ():
        faces = np.zeros(shape=(1,1))
    print(faces)
        
    avg_y = avg_y // faces.shape[0]
    avg_x = avg_x // faces.shape[0]
    
    print(avg_x, avg_y)
    return faces
    
    
    

while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    cv2.imshow(
        "My Face Detection Project", video_frame
    )  # display the processed frame in a window named "My Face Detection Project"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()

# pseudo code: 1. loop, in which we calculate the average face location, 
# in which the break condition for the loop will be if the average is in the center of the resolution 
# if yavg > 540 then bring the camera down with servo no 2 
# if xavg > 960 then bring the camera right 
# if both > then first do y adn then x 