import requests
url = "https://api.travelpayouts.com/v2/prices/month-matrix"
querystring = {"currency":"usd","show_to_affiliates":"true","origin":"NYC","destination":"LAX"}
headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}
response = requests.request("GET", url, headers=headers, params=querystring)
a = response.json()
print(a)

a.keys()

print(a["data"]["depart_date"])