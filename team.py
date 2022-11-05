import requests
import json

def search_team(tname, tteams_list):
        # teams data is returned as dictionaries
        for entry in tteams_list:
            if entry['name'] == tname:
                return entry
        return None

    # remember to look how to return '404 error' above instead of None

