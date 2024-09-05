'''
Choose an API from RapidAPI that interests you—make sure it has a free tier and simple authentication. 
Write a Python script that makes a request to your selected API, 
using the appropriate endpoint and parameters to retrieve data. 
Save the response data to a variable, and handle it as JSON to work with nested structures. 
Extract a specific item from the nested dictionary in the response, 
and print a statement that meaningfully displays this information. 
Have fun exploring the data you retrieve!
'''

import requests

url = "https://emotion-detection2.p.rapidapi.com/emotion-detection"

payload1 = { "url": "https://as2.ftcdn.net/v2/jpg/00/56/93/53/1000_F_56935312_NiqxkRKOdGSJd86Tc2uLycL9fkUsIlRW.jpg" }

# payload2 = { "url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80" }

payload2 = {"url": "https://live-production.wcms.abc-cdn.net.au/4cc0c19aad68a86fac83bf86dcba4a6f?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=353&width=862&height=485"}

def emotion_detection(payload):
    headers = {
        "x-rapidapi-key": "7151a85feamsh3022275bdbb665fp1c8c0bjsn06b5ae28ea16",
        "x-rapidapi-host": "emotion-detection2.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    var = response.json()

    for item in var:
        # print(item)
        if item["probability"] >= 0.99:
            # print(f"The emotion presented in the picture is {item["emotion"]["value"]}")
            return item["emotion"]["value"]
        else:
            print("Probability is less than 0.99, Cannot detect Correct emotion")
            return None

print("The first image emotion is", emotion_detection(payload1))
print("the second image emotion is", emotion_detection(payload2))

