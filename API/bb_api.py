import requests

url = "https://bb-finance.p.rapidapi.com/stock/get-statistics"

querystring = {"id":"aapl:us","template":"STOCK"}

headers = {
	"x-rapidapi-key": "7151a85feamsh3022275bdbb665fp1c8c0bjsn06b5ae28ea16",
	"x-rapidapi-host": "bb-finance.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
# Function to extract a value by name
def extract_value(data, field_name):
    for item in data['result'][0]['table']:
        print(item)
        if item['name'] == field_name:
            print(f"Current P/E Ratio: {item['value']}")
            return item['value']
    return None


extract_value(data, 'Current P/E Ratio (ttm)')
