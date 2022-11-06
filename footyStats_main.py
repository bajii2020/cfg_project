"""
IMPORTS
"""
from website import create_app
from flask import Flask, jsonify, request
# from test_data import teams
# from team import search_team
from client_main import get_team, table_result, get_lineups, match_result, display_table

"""
APP INIT
"""
app = create_app()
#app = Flask(__name__)

"""
ENDPOINTS
"""
@app.route('/team/<string:name>')
def get_team_by_name(name):
    team = get_team(name)
    return jsonify(team)


# @app.route('/teams')
# def get_team():
#     for team in response:
#         print(team)
#         return jsonify(team)


@app.route('/table')
def table():
    results = table_result()
    return jsonify(results)
# def table():
#     result = display_table()
#     return jsonify(result)

@app.route('/formations/<string:team1><string:team2>')
def lineups(team1, team2):
    lineups_data = get_lineups(team1, team2)
    return jsonify(lineups_data)


@app.route('/matchday/<string:id>')
def matchday(matchdayid):
    matchday_res = match_result(matchdayid)
    return jsonify(matchday_res)


"""
RUN
"""
if __name__ == '__main__':
    app.run(debug=True)
