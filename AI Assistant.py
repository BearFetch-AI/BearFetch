import requests

print("Welcome to your local AI assistant (powered by Ollama)")
print("Type 'exit' to quit.\n")

while True:
    user_prompt = input("Enter your prompt: ")

    if user_prompt.strip().lower() in ['exit', 'quit']:
        print("Goodbye.")
        break

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",  # Change to "llama3" or others if needed
                "prompt": user_prompt,
                "stream": False
            }
        )

        if response.status_code == 200:
            data = response.json()
            print("\nResponse:\n" + data.get("response", "No response found.") + "\n")
        else:
            print("Error:", response.status_code)
            print(response.text)

    except Exception as e:
        print("Error communicating with Ollama:", e)
