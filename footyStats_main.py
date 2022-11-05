"""
IMPORTS
"""
from website import create_app
from flask import Flask, jsonify, request
# from test_data import teams
# from team import search_team
from client_main import get_team, table_result, get_lineups, match_result

"""
APP INIT
"""
app = create_app()


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
def table_result():
    results = table_result()
    # #table = table_result()
    return jsonify(results)


@app.route('/formations/<string:team1><string:team2>')
def get_lineups(team1, team2):
    lineups = get_lineups(team1, team2)
    return jsonify(lineups)


@app.route('/matchday/<string:id>')
def matchday(matchdayid):
    matchday_res = match_result(matchdayid)
    return jsonify(matchday_res)


"""
RUN
"""
if __name__ == '__main__':
    app.run(debug=True)
