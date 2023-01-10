import requests
API_key="141710af2113bab9f55ef73e1bcd33d5"


# example: getData(New York, 4, temperature)
def getData(place, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()

    filtereddata = data['list']
    n_values = 8*days
    filtereddata = filtereddata[:n_values]

    return filtereddata

if __name__ == "__main__":
    print(getData(place="Jabalpur", days=3))