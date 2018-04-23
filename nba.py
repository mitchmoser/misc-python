#!/usr/bin/env python3
# NBA API Documentation:
# https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation

import json
import requests
import operator

url="http://stats.nba.com/stats/teamyearbyyearstats/"
params={
        "LeagueID":"00",  # NBA=00 ABA=01
        "SeasonType":"Regular Season",
        "Permode":"Totals",
        "TeamID":1610612747  # LA Lakers
       }

# API requires a header... any header
headers = {'User-Agent': 'My User Agent 1.0'}

# send request for json data
r = requests.get(url, params=params, headers=headers)
data = json.loads(r.text)

# this is what is returned
resultSets = data['resultSets'][0]['rowSet']

wins = {}  # season year : number of wins

# return year w/ most wins
for season in resultSets:
    years = season[3]
    count = season[5]
    wins[years] = count

mostWins = max(wins, key=wins.get)
teamName = f'{resultSets[-1][1]} {resultSets[-1][2]}'
print(f'The {mostWins} regular season had the most wins for the {teamName}')

# pull extra details for that season
for season in resultSets:
    if mostWins == season[3]:
        print("%-17s : %s" % ("Wins", season[5]))
        print("%-17s : %s" % ("Losses", season[6]))
        print("%-17s : %s" % ("Win Percentage", season[7]))
        print("%-17s : %s" % ("Conference Rank", season[12]))
        print("%-17s : %s" % ("Division Rank", season[13]))
        print("%-17s : %s" % ("Finals Appearance", season[14]))
