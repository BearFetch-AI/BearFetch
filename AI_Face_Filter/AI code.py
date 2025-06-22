import cv2
import os
import sys
import numpy as np


base_path = "/Users/sachin/Documents/AI filter test/AI_Face_Filter/"
face_path = os.path.join(base_path, "haarcascade_frontalface_default.xml")
eye_path = os.path.join(base_path, "haarcascade_eye.xml")
glasses_path = os.path.join(base_path, "_Pngtree_black_frame_hexagon_square_eye_7326001-removebg-preview.png")  


face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade = cv2.CascadeClassifier(eye_path)

if face_cascade.empty():
    print("❌ ERROR: Could not load face cascade.")
    sys.exit()

if eye_cascade.empty():
    print("❌ ERROR: Could not load eye cascade.")
    sys.exit()


glasses = cv2.imread(glasses_path, cv2.IMREAD_UNCHANGED)
if glasses is None or glasses.shape[2] != 4:
    print(f"❌ ERROR: Could not load glasses image with alpha channel: {glasses_path}")
    sys.exit()


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ ERROR: Could not open webcam.")
    sys.exit()


def overlay_image_alpha(background, overlay, x, y, size):
    overlay_resized = cv2.resize(overlay, size)

    b, g, r, a = cv2.split(overlay_resized)
    overlay_rgb = cv2.merge((b, g, r))
    mask = a / 255.0

    h, w = overlay_rgb.shape[:2]
    if y + h > background.shape[0] or x + w > background.shape[1]:
        return  

    roi = background[y:y+h, x:x+w].astype(float)
    overlay_rgb = overlay_rgb.astype(float)


    for c in range(3):  # R, G, B
        roi[:, :, c] = roi[:, :, c] * (1 - mask) + overlay_rgb[:, :, c] * mask

    background[y:y+h, x:x+w] = roi.astype(np.uint8)


while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ ERROR: Failed to capture video frame.")
        break

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) >= 2:
          
            glasses_x = x
            glasses_y = y + int(h / 4.5)
            glasses_w = w
            glasses_h = int(h / 3)
            overlay_image_alpha(frame, glasses, glasses_x, glasses_y, (glasses_w, glasses_h))

    cv2.imshow("Your AI Filter!", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
