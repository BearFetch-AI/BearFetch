import cv2

# Load the AI face and eye detectors
face_cascade = cv2.CascadeClassifier("/Users/sachin/Documents/AI filter test/AI_Face_Filter/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Load the glasses image
glasses = cv2.imread('_Pngtree_black_frame_hexagon_square_eye_7326001-removebg-preview.png', -1)

# Start your webcam
cap = cv2.VideoCapture(0)

# Function to put glasses on your face
def overlay_image(background, overlay, x, y, w, h):
    overlay = cv2.resize(overlay, (w, h))
    for i in range(h):
        for j in range(w):
            if overlay[i, j][3] != 0:  # Not transparent
                background[y+i, x+j] = overlay[i, j][:3]

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        eyes = eye_cascade.detectMultiScale(frame[y:y+h, x:x+w])
        if len(eyes) >= 2:
            overlay_image(frame, glasses, x, y + int(h/4), w, int(h/3))

    cv2.imshow("Your AI Filter!", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
