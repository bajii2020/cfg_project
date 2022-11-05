import requests
import json

import lxml
import requests
from bs4 import BeautifulSoup
import re
import time
from pprint import pprint

baselink = f"https://onefootball.com/en/competition/premier-league-9/table"
endpoint  = 'table'

def display_table():
    source = requests.get(baselink+endpoint).text
    page = BeautifulSoup(source, "lxml")
    tab = page.find_all("a", class_="standings__row-grid")
    table = []
    table.append("  _____TEAM_______ PL W D L GD PTS")

    for i in range(len(tab)):
        table.append(tab[i].text.strip())
        # pprint(table)

    return table

# https://rapidapi.com/heisenbug/api/premier-league-live-scores/details
baseurl = "https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/"

headers = {
    "X-RapidAPI-Key": "0546136983mshf1b2571a6e03047p1d321bjsn62ce1e5f9762",
    "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
}

# team, takes team name
def get_team(team_name):
    endpoint_team = "team"
    querystring = {"name": team_name}
    response = requests.request("GET", (baseurl + endpoint_team), headers=headers, params=querystring)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return f"Error: {response.status_code}"


# league_table, no parameters
def table_result():
    endpoint_table = "table"
    response = requests.request("GET", baseurl + endpoint_table, headers=headers)
    data = json.loads(response.text)
    return data


# lineups, takes two team names
def get_lineups(team1, team2):
    endpoint_lineups = "formations"
    querystring = {"team1": team1,"team2": team2}
    response = requests.request("GET", baseurl+endpoint_lineups, headers=headers, params=querystring)
    data = json.loads(response.text)
    return data


# match, takes match day ID, day 1 = Aug 05 2022
def match_result(match_day_id):
    querystring = {"matchday": match_day_id}
    response = requests.request("GET", baseurl, headers=headers, params=querystring)
    data = json.loads(response.text)
    return data



