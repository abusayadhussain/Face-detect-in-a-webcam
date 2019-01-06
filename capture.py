import cv2

video = cv2.VideoCapture(0)
a=0
face_casscade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    a=a+1
    check, frame = video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_casscade.detectMultiScale(gray, scaleFactor = 1.70, minNeighbors=5)
    for x,y,w,h in faces:
        img = cv2.rectangle(frame, (x,y), (x+w,y+h), (71,99,255),3)
    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(100)

    if key ==ord('q'):
        break;
print(a)
video.release()
cv2.destroyAllWindows
