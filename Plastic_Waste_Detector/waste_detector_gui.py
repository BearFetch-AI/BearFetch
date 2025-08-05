import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load model (adjust path if needed)
model = YOLO("/Users/sachin/Documents/AI filter test/Plastic_Waste_Detector/train2/weights/best.pt")

def calculate_trashiness(boxes, img_shape):
    total_area = img_shape[0] * img_shape[1]
    detected_area = sum((x2 - x1) * (y2 - y1) for (x1, y1, x2, y2) in boxes)
    return (detected_area / total_area) * 100 if total_area > 0 else 0

def detect_and_display(img_path):
    results = model(img_path, conf=0.3)[0]
    img_bgr = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    boxes = []
    for box in results.boxes.xyxy.cpu().numpy():
        x1, y1, x2, y2 = box[:4].astype(int)
        boxes.append((x1, y1, x2, y2))
        cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (0, 255, 0), 2)

    trashiness = calculate_trashiness(boxes, img_rgb.shape)
    return img_rgb, trashiness

def show_image(img_array):
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.imshow(img_array)
    ax.axis('off')

    canvas = FigureCanvasTkAgg(fig, master=image_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    return canvas

def upload_image():
    for widget in image_frame.winfo_children():
        widget.destroy()
    file_path = filedialog.askopenfilename()
    if file_path:
        img_array, score = detect_and_display(file_path)
        show_image(img_array)
        trash_label.config(text=f"Trashiness Score: {score:.2f}%")

# GUI setup
root = tk.Tk()
root.title("Waste Detector")

upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

trash_label = tk.Label(root, text="Trashiness Score: N/A", font=("Arial", 14))
trash_label.pack()

image_frame = tk.Frame(root)
image_frame.pack()

root.mainloop()
