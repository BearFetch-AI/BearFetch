import cv2
import os
import sys

# === Full Paths ===
base_path = "/Users/sachin/Documents/AI filter test/AI_Face_Filter/"
face_path = os.path.join(base_path, "haarcascade_frontalface_default.xml")
eye_path = os.path.join(base_path, "haarcascade_eye.xml")
glasses_path = os.path.join(base_path, "_Pngtree_black_frame_hexagon_square_eye_7326001-removebg-preview.png")

# === Load Cascades ===
face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade = cv2.CascadeClassifier(eye_path)

if face_cascade.empty():
    print("❌ ERROR: Could not load face cascade.")
    sys.exit()

if eye_cascade.empty():
    print("❌ ERROR: Could not load eye cascade.")
    sys.exit()

# === Load Glasses PNG with Alpha Channel ===
glasses = cv2.imread(glasses_path, cv2.IMREAD_UNCHANGED)
if glasses is None or glasses.shape[2] != 4:
    print(f"❌ ERROR: Could not load glasses image from: {glasses_path}")
    sys.exit()

# === Start Webcam ===
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ ERROR: Could not open webcam.")
    sys.exit()

# === Overlay Transparent PNG ===
def overlay_image_alpha(img, img_overlay, x, y, overlay_size):
    overlay = cv2.resize(img_overlay, overlay_size)

    b, g, r, a = cv2.split(overlay)
    overlay_rgb = cv2.merge((b, g, r))
    mask = cv2.merge((a, a, a))

    h, w = overlay_rgb.shape[:2]
    roi = img[y:y+h, x:x+w]

    # Blend overlay within the region of interest
    img[y:y+h, x:x+w] = cv2.addWeighted(roi, 1 - a/255.0, overlay_rgb, a/255.0, 0)

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
            try:
                overlay_image_alpha(frame, glasses, x, y + int(h / 4), (w, int(h / 3)))
            except:
                pass  # Avoid crash if dimensions are off-screen

    cv2.imshow("Your AI Filter!", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
