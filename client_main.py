import requests
import json
import pprint as pp

def get_team():
    url = "https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/team"
    querystring = {"name": "Liverpool"}
    headers = {
        "X-RapidAPI-Key": "0546136983mshf1b2571a6e03047p1d321bjsn62ce1e5f9762",
        "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = json.loads(response.text)
        print(data)
    else:
        print(f"Error: {response.status_code}")

def run():
    get_team()

if __name__ == '__main__':
    run()