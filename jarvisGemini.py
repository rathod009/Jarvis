from config import key
import requests  # web
from speech import mic

def chat1(chat):
    if chat is None:
        print("No speech recognized. Please try again.")
        return
    
    messages = []  # list of all the chats
    system_message = "You are an AI bot, Your name is Jarvis"
    message = {"role": "user", "parts": [{"text": system_message + " " + chat}]}
    messages.append(message)
    data = {"contents": messages}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + key
    response = requests.post(url, json=data)

    if response.status_code == 404:
        print("Error 404: Endpoint not found.")
    elif response.status_code == 200:
        t1 = response.json()
        t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
        print(t2)
    else:
        print("Error:", response.status_code)

while True:
    chat = mic()
    #chat = input("Enter the Query: ")
    # chat = "who is MS Dhoni"
    #chat1(chat)

    if chat:
        chat1(chat)
        break  # Exit the loop if speech is recognized
    else:
        print("No speech recognized. Please try again.")
        break