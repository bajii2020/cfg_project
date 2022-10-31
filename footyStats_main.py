"""
IMPORTS
"""
from website import create_app
from flask import Flask, jsonify, request
#from team_code import teams
from team import search_team
from client_main import get_team
# import here auth?

"""
INTITIALISE THE APP
"""
app = create_app()

"""
ENDPOINTS
"""
@app.route('/teams')
def get_team():
    for team in teams:
        print(team)
        return jsonify(team)

@app.route('/team/<string:name>')
def get_team_by_name(name):
    team = search_team(name, teams)
    return jsonify(team)

"""
RUN
"""
if __name__ == '__main__':
    app.run(debug=True)
