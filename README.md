# 🐻 BearFetch

**BearFetch** is an educational project designed to teach **middle school students** — especially those from **underprivileged backgrounds** — the foundations of **Artificial Intelligence** through fun, interactive Python projects.

From building an AI-powered Snapchat-style face filter to coding an unbeatable Tic-Tac-Toe game, BearFetch offers hands-on learning that makes AI exciting and accessible to kids.

---

## ✨ Features

- 🎭 Build your own Snapchat-style face filter
- 🕹️ Play against an unbeatable AI in Tic-Tac-Toe
- 🧠 Learn real AI techniques using Python and OpenCV
- 👦 Designed for kids and first-time coders
- 💻 Offline-friendly: great for classrooms

---

## 📦 Required Downloads Before Running

Before using any project, make sure you have these files and tools installed.

### 🔧 1. Install Python (3.7+)
- [Download Python](https://www.python.org/downloads/)
- Ensure Python and `pip` are available in your terminal

### 🧠 2. Download OpenCV Haarcascade Files
These are used for face and eye detection in the AI filter.

📥 Download these XML files:
- [`haarcascade_frontalface_default.xml`](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- [`haarcascade_eye.xml`](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

📂 Save them in the **same folder** as your Python file.

### 🖼️ 3. Download Glasses PNG (for the face filter)
Use your own PNG or download a free sample like:
- [`glasses.png`](https://www.pngmart.com/files/7/Glasses-PNG-Pic.png) (rename as needed)

---

## 🧠 Optional: Ollama (for advanced AI experiments)

> Only needed if you're experimenting with local language models.

**Ollama** is a tool for running AI models (like LLaMA) locally on your computer.

📥 [Download Ollama here](https://ollama.com/)

To install (macOS):
```bash
brew install ollama

Installing Python Dependencies:
pip install opencv-python pygame

If pip doesn't work then do : python3 -m pip install opencv-python pygame

Also most projects can be run using this command: python3 main.py

To pull a model use this: ollama pull llama2

