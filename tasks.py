from config import key
import requests
import socket

def get_ip(host):
    try:
        return socket.getaddrinfo("google.com", None)
    except Exception as e:
        print(e)
        result = f"Error in finding the IP, {e}"
    return result
    

def temp_room(room):
    result = "Humidity: 54, Temp in C: 24.87"
    return result

def get_weather(city):
    #endpoint for getting weather data from yahoo weather
    url = "https://yahoo-weather5.p.rapidapi.com/weather" 

    querystring = {"location":city,"format":"json","u":"f"}

    headers = {
        "X-RapidAPI-Key": "Replace this Text with your RapidAPI-Key if you want to use my project.",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    d1 = response.json() #return the weather data in json format
    d1 = d1.get("current_observation")
    hum = d1.get('atmosphere').get('humidity')
    temp = d1.get('condition').get('temperature')
    temp = (temp - 32) * 5.0/9.0 
    temp = round(temp, 2)
    return (f"Humidity: {hum}, Temp in C: {temp}")

def chat1(chat):
    if chat is None:
        print("No speech recognized. Please try again.")
        return
    
    messages = []  # list of all the chats
    system_message = "You are an AI bot, Your name is Jarvis. Find the content related to the chat. If you need help type 'help' or say 'Hello', so far I can find the weather of a city, temperature of a room and IP address of a domain name."
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
        return t2
    else:
        print("Error:", response.status_code)

definitions = [
    {
        "name": "chat1",
        "description": "Hi Hello General Message",
        "parameters": {
            "type": "object",
            "properties": {
                "chat": {
                    "type": "string",
                    "description": "Full Query Aksed by the User."
                }
            }
        }
    },
    {
        "name": "get_weather",
        "description": "Find weather and temperature of a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name to find weather."
                }
            }
        }
    },
    {
        "name": "temp_room",
        "description": "Find temperature and humidity of a room.",
        "parameters": {
            "type": "object",
            "properties": {
                "room": {
                    "type": "string",
                    "description": "Room or home."
                }
            }
        }
    },
    {
        "name": "get_ip",
        "description": "Find IP Address of given URL or Domain name",
        "parameters": {
            "type": "object",
            "properties": {
                "host": {
                    "type": "string",
                    "description": "Get URL or Domain name"
                }
            }
        }
    }
]


#printing out the function result
if __name__ == "__main__":
    print(get_weather("Anand")) 
    print(temp_room("Room"))
