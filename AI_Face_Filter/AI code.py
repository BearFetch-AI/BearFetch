import cv2
import os
import sys

# === Load Haar Cascades ===
face_path = "/Users/sachin/Documents/AI filter test/AI_Face_Filter/haarcascade_frontalface_default.xml"
eye_path = "/Users/sachin/Documents/AI filter test/AI_Face_Filter/haarcascade_eye.xml"
glasses_path = "/Users/sachin/Documents/AI filter test/AI_Face_Filter/glasses.png"  # Rename for simplicity

# Load cascades
face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade = cv2.CascadeClassifier(eye_path)

# Safety checks
if face_cascade.empty():
    print("❌ ERROR: Could not load face cascade.")
    sys.exit()

if eye_cascade.empty():
    print("❌ ERROR: Could not load eye cascade.")
    sys.exit()

# === Load Glasses PNG ===
glasses = cv2.imread(glasses_path, -1)
if glasses is None:
    print("❌ ERROR: Glasses image not found or failed to load.")
    sys.exit()

# === Start Webcam ===
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ ERROR: Could not open webcam.")
    sys.exit()

# === Function to Overlay Glasses ===
def overlay_image(background, overlay, x, y, w, h):
    overlay = cv2.resize(overlay, (w, h))
    for i in range(h):
        for j in range(w):
            if y + i >= background.shape[0] or x + j >= background.shape[1]:
                continue  # prevent overflow
            if overlay[i, j][3] != 0:  # Check alpha channel
                background[y + i, x + j] = overlay[i, j][:3]

# === Main Loop ===
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
            overlay_image(frame, glasses, x, y + int(h / 4), w, int(h / 3))

    cv2.imshow("Your AI Filter!", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === Cleanup ===
cap.release()
cv2.destroyAllWindows()
