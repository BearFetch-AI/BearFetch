import tkinter as tk
from tkinter import scrolledtext
import requests
import threading

# Function to send prompt to Ollama
def ask_ollama():
    chat_log.config(state=tk.NORMAL)

    prompt = input_box.get()
    if prompt.strip().lower() in ['exit', 'quit']:
        window.quit()
        return

    chat_log.insert(tk.END, f"You: {prompt}\n")
    input_box.delete(0, tk.END)

    def get_response():
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "gemma:2b",  # or "llama3"
                    "prompt": prompt,
                    "stream": False
                }
            )
            if response.status_code == 200:
                reply = response.json().get("response", "[No response]")
                chat_log.insert(tk.END, f"Ollama: {reply.strip()}\n\n")
                chat_log.config(state=tk.NORMAL)

            else:
                chat_log.insert(tk.END, "Ollama: Error from API.\n\n")
        except Exception as e:
            chat_log.insert(tk.END, f"Ollama: Failed to connect ({e})\n\n")

    
    threading.Thread(target=get_response).start()
    chat_log.insert(tk.END, "\nType exit or quit to exit the window\n")


# GUI setup
window = tk.Tk()
window.title("Bearfetch AI")
window.geometry("600x500")
window.configure(bg="#b5cde8")

chat_log = tk.Text(window, wrap=tk.WORD, font=("Open Sans", 12), bg="#d2b48c", fg="#1a2b3c", padx=10, pady=10)
chat_log.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(window, bg="#2e3a59")
input_frame.pack(fill=tk.X, padx=0, pady=0)

input_box = tk.Entry(input_frame, font=("Open Sans", 12), bg="#d2b48c", fg="#FFFFFF")
input_box.config(borderwidth=5, relief="ridge")
input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 0))

send_button = tk.Button(input_frame, text="Send", font=("Open Sans", 12), bg="#0080ff", fg="#000000", command=ask_ollama)
send_button.pack(side=tk.RIGHT)

input_box.bind("<Return>", lambda event: ask_ollama())

chat_log.insert(tk.END, "\nType exit or quit to exit the window\n")

chat_log.config(state=tk.DISABLED)

window.mainloop()
