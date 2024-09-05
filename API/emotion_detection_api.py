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

payload2 = { "url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80" }


def emotion_detection(payload):
    headers = {
        "x-rapidapi-key": "7151a85feamsh3022275bdbb665fp1c8c0bjsn06b5ae28ea16",
        "x-rapidapi-host": "emotion-detection2.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    var = response.json()

    print(f"The emotion presented in the picture is {var[0]["emotion"]["value"]}")

emotion_detection(payload1)
emotion_detection(payload2)

