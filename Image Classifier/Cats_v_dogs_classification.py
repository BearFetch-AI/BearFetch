import tensorflow
from tensorflow import keras
from keras.models import load_model  # Best to use TensorFlow import
from PIL import Image, ImageOps  # Pillow for image handling
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# ✅ Load the trained model
model = load_model("/Users/sachin/Documents/AI\ filter \test/Image\ Classifier/converted_keras copy/keras_model.h5", compile=False)

# ✅ Load labels
with open("/Users/sachin/Documents/AI filter test/Image Classifier/converted_keras copy/labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# ✅ Create input array
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# ✅ Replace this with the path to your image
image_path = "/Users/sachin/Documents/AI filter test/Image Classifier/test_images/dog.4001.jpg"

# ✅ Load & preprocess image
image = Image.open(image_path).convert("RGB")

# Resize to 224x224
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# Convert to numpy & normalize [-1, 1]
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load into input array
data[0] = normalized_image_array

# ✅ Make prediction
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

print("Class:", class_name)
print("Confidence Score:", confidence_score)
