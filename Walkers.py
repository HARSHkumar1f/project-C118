import cv2
body_cascade = cv2.CacadeClassifire("haarcascade_fullbody.xml")

# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    body = body_cascade.detectMultiScale(gray)

    
    # Extract bounding boxes for any bodies identified
    for (x, y , w, h) in body:
        cv2.rectngle(frame, (x,y),(x+w, y+h), (255,0,90), 1)
    cv2.imshow("Web cam",body)
    if cv2.waitKey(25) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
