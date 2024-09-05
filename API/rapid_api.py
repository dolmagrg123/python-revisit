import requests

url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

querystring = {"Category":"tennis","Timezone":"-7"}

headers = {
	"x-rapidapi-key": "7151a85feamsh3022275bdbb665fp1c8c0bjsn06b5ae28ea16",
	"x-rapidapi-host": "livescore6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

raw = response.json()
# print(raw)

print(raw["Stages"])

for item in raw["Stages"]:
    print("")
    # print(item)
    # print({item.get("Sid")})
    # print(item["Sid"])
