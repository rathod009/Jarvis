# This file will execute the respective function based on user's query.
# For example, if user asks "What is the weather in Delhi?" then this file will execute the function to get the weather in Delhi.
# Similarly, if user asks "What is the temperature in the room?" then this file will execute the function to get the temperature in the room.

import tasks
from config import key
import requests
from speech import mic

def parse_func_resp(message):
    function_call = message[0]['functionCall']
    function_name = function_call['name']
    print("Gemini: call function", function_name)
    try:
        arguments = function_call.get('args', {"location": "Delhi"})  # Provide default arguments if not present
        print("Gemini: arguments", arguments)
        if arguments:
            func = getattr(tasks, function_name)
            print("Gemini: function", func)
            function_response = func(**arguments)
        else:
            function_response = "No Arguments are Present"
    except Exception as e:
        print("Error: ", e)
        function_response = "Error: " + str(e)
    return function_response


            
def run_conversation(user_message):
    messages = []  # List all messages
    print(user_message)
    system_message = """You are an AI bot that can do everything using function call. 
    When you are asked to do something, use the function call you have available and 
    then respond with message"""  # First instruction

    message = {"role" : "user",
               "parts" : [{"text": system_message+ "\n" + user_message}]}

    messages.append(message)

    data = {"contents" : [message],
            "tools" : 
        [{  "functionDeclarations" : tasks.definitions }]
        }

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + key
    response = requests.post(url, json=data)

    if response.status_code != 200:
        print(response.text)
        return "Error: Unable to process the request."

    t1 = response.json()
    if "content" not in t1.get("candidates")[0]:
        print("Error: No Content in Response")
        return "Error: No Content in Response"
    
    message = t1.get("candidates")[0].get("content").get("parts")
    print("Message ########: ", message)
    if 'functionCall' in message[0]: 
        resp1 = parse_func_resp(message)
        print("Actual: response", resp1)
        # mic()
        return resp1
    else: 
        print("No Function Call")
        
if __name__ == "__main__":
    user_message = "find the weather of Delhi"
    print(run_conversation(user_message))

    # user_message = "find the temperature of My Room"
    # print(run_conversation(user_message))
    
    # user_message = "find the IP Address of Google.com"
    # print(run_conversation(user_message))
    