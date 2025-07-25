import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import numpy as np
from tensorflow.keras.models import load_model

# Load model and labels
model = load_model("keras_model.h5", compile=False)
with open("labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Preprocessing function
def preprocess_image(image_path):
    size = (224, 224)
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data, image

# Prediction function
def predict_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    data, pil_image = preprocess_image(file_path)
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Update image
    img_display = pil_image.resize((250, 250))
    tk_image = ImageTk.PhotoImage(img_display)
    image_label.configure(image=tk_image)
    image_label.image = tk_image

    # Update result
    result_text.set(f"{class_name}\nConfidence: {confidence_score*100:.2f}%")

# GUI Setup
window = tk.Tk()
window.title("🐶 Cat vs Dog Classifier 🐱")
window.geometry("500x550")
window.configure(bg="#f5f0e6")  # Light tan background

# Fonts & Colors
TITLE_FONT = ("Helvetica", 20, "bold")
RESULT_FONT = ("Helvetica", 14)
BUTTON_FONT = ("Helvetica", 12)

# Title
title_label = tk.Label(window, text="🐾 AI Pet Classifier", font=TITLE_FONT, bg="#f5f0e6", fg="#5c4033")  # Deep brown
title_label.pack(pady=15)

# Result display
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=RESULT_FONT, bg="#ffffff", fg="#3b82f6",  # Blue text
                        width=40, height=4, relief="groove", bd=2)
result_label.pack(pady=10)

# Upload button
btn = tk.Button(window, text="Upload Image", font=BUTTON_FONT, command=predict_image,
                bg="#8b5e3c", fg="black", activebackground="#a86d4d", padx=10, pady=5)
btn.pack(pady=10)

# Image preview
image_label = tk.Label(window, bg="#f5f0e6")
image_label.pack(pady=10)

# Run the app
window.mainloop()
