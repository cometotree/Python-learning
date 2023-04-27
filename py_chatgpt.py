import requests
import json

url = "https://api.chatgpt.com/generate/"

api_key = "YOUR_API_KEY"

def GPTAnswer(prompt):
    payload = {
        "prompt": prompt,
        "length": 50,
        "api_key": "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"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result["text"]
    else:
        print("Error:", response.status_code)

# Example usage
# prompt = input("Enter your prompt: ")
answer = GPTAnswer("Please translate hello into Chinese.")
print(answer)