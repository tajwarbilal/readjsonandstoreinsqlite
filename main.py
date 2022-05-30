# Python program to read
# json file

import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hellohowareyou'

# sqlalchemy .db location (for sqlite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# sqlalchemy track modifications in sqlalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Fixture(db.Model):
    __tablename__ = 'fixture'
    iduni = db.Column(db.Integer, primary_key=True)
    fix_id = db.Column(db.String(15))
    referee = db.Column(db.String(15))
    timezone = db.Column(db.String(50))
    date = db.Column(db.String(80))
    timestamp = db.Column(db.String(80))
    periods_first = db.Column(db.String(80))
    periods_second = db.Column(db.String(80))
    venue_id = db.Column(db.String(80))
    venue_name = db.Column(db.String(80))
    venue_city = db.Column(db.String(80))
    status_long = db.Column(db.String(80))
    status_short = db.Column(db.String(80))
    status_elapsed = db.Column(db.String(80))
    league_id = db.Column(db.String(80))
    league_name = db.Column(db.String(80))
    league_country = db.Column(db.String(80))
    league_season = db.Column(db.String(80))
    league_round = db.Column(db.String(80))
    teams_home_id = db.Column(db.String(80))
    teams_home_name = db.Column(db.String(80))
    teams_home_winner = db.Column(db.String(80))
    teams_away_id = db.Column(db.String(80))
    teams_away_name = db.Column(db.String(80))
    teams_away_winner = db.Column(db.String(80))
    goal_home = db.Column(db.String(80))
    goals_away = db.Column(db.String(80))
    scores_halftime_home = db.Column(db.String(80))
    scores_halftime_away = db.Column(db.String(80))
    scores_fulltime_home = db.Column(db.String(80))
    scores_fulltime_away = db.Column(db.String(80))
    scores_extratime_home = db.Column(db.String(80))
    scores_extratime_away = db.Column(db.String(80))
    scores_penalty_home = db.Column(db.String(80))
    scores_penalty_away = db.Column(db.String(80))

    def __init__(self, fix_id, referee, timezone, date, timestamp, periods_first, periods_second,
                 venue_id, venue_name, venue_city, status_long, status_short, status_elapsed,
                 league_id, league_name, league_country, league_season, league_round, teams_home_id,
                 teams_home_name, teams_home_winner, teams_away_id, teams_away_name, teams_away_winner,
                 goal_home, goals_away, scores_halftime_home, scores_halftime_away, scores_fulltime_home,
                 scores_fulltime_away, scores_extratime_home, scores_extratime_away, scores_penalty_home,
                 scores_penalty_away
                 ):
        self.fix_id = fix_id
        self.referee = referee
        self.timezone = timezone
        self.date = date
        self.timestamp = timestamp
        self.periods_first = periods_first
        self.periods_second = periods_second
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.venue_city = venue_city
        self.status_long = status_long
        self.status_short = status_short
        self.status_elapsed = status_elapsed
        self.league_id = league_id
        self.league_name = league_name
        self.league_country = league_country
        self.league_season = league_season
        self.league_round = league_round
        self.teams_home_id = teams_home_id
        self.teams_home_name = teams_home_name
        self.teams_home_winner = teams_home_winner
        self.teams_away_id = teams_away_id
        self.teams_away_name = teams_away_name
        self.teams_away_winner = teams_away_winner
        self.goal_home = goal_home
        self.goals_away = goals_away
        self.scores_halftime_home = scores_halftime_home
        self.scores_halftime_away = scores_halftime_away
        self.scores_fulltime_home = scores_fulltime_home
        self.scores_fulltime_away = scores_fulltime_away
        self.scores_extratime_home = scores_extratime_home
        self.scores_extratime_away = scores_extratime_away
        self.scores_penalty_home = scores_penalty_home
        self.scores_penalty_away = scores_penalty_away


db.create_all()
db.session.commit()

# Opening JSON file
f = open('fixtures.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    try:
        new_data = Fixture.query.filter_by(fix_id=i['fixture']['id']).first()
    except:
        print('do nothing')

    if new_data:
        new_data.fix_id = str(i['fixture']['id'])
        new_data.referee = str(i['fixture']['referee'])
        new_data.timezone = str(i['fixture']['timezone'])
        new_data.date = str(i['fixture']['date'])
        new_data.timestamp = str(i['fixture']['timestamp'])
        new_data.periods_first = str(i['fixture']['periods']['first'])
        new_data.periods_second = str(i['fixture']['periods']['second'])
        new_data.venue_id = str(i['fixture']['venue']['id'])
        new_data.venue_name = str(i['fixture']['venue']['name'])
        new_data.venue_city = str(i['fixture']['venue']['city'])
        new_data.status_long = str(i['fixture']['status']['long'])
        new_data.status_short = str(i['fixture']['status']['short'])
        new_data.status_elapsed = str(i['fixture']['status']['elapsed'])
        new_data.league_id = str(i['league']['id'])
        new_data.league_name = str(i['league']['name'])
        new_data.league_country = str(i['league']['country'])
        new_data.league_season = str(i['league']['season'])
        new_data.league_round = str(i['league']['round'])
        new_data.teams_home_id = str(i['teams']['home']['id'])
        new_data.teams_home_name = str(i['teams']['home']['name'])
        new_data.teams_home_winner = str(i['teams']['away']['winner'])
        new_data.teams_away_id = str(i['teams']['away']['id'])
        new_data.teams_away_name = str(i['teams']['away']['name'])
        new_data.teams_away_winner = str(i['teams']['away']['winner'])
        new_data.goal_home = str(i['goals']['home'])
        new_data.goals_away = str(i['goals']['away'])
        new_data.scores_halftime_home = str(i['score']['halftime']['home'])
        new_data.scores_halftime_away = str(i['score']['halftime']['away'])
        new_data.scores_fulltime_home = str(i['score']['fulltime']['home'])
        new_data.scores_fulltime_away = str(i['score']['fulltime']['away'])
        new_data.scores_extratime_home = str(i['score']['extratime']['home'])
        new_data.scores_extratime_away = str(i['score']['extratime']['away'])
        new_data.scores_penalty_home = str(i['score']['penalty']['home'])
        new_data.scores_penalty_away = str(i['score']['penalty']['away'])
        db.session.commit()
        print(new_data, 'Record already exsist and updated')
    else:
        new_user = Fixture(fix_id=i['fixture']['id'],
                           referee=i['fixture']['referee'],
                           timezone=i['fixture']['timezone'],
                           date=i['fixture']['date'],
                           timestamp=i['fixture']['timestamp'],
                           periods_first=i['fixture']['periods']['first'],
                           periods_second=i['fixture']['periods']['second'],
                           venue_id=i['fixture']['venue']['id'],
                           venue_name=i['fixture']['venue']['name'],
                           venue_city=i['fixture']['venue']['city'],
                           status_long=i['fixture']['status']['long'],
                           status_short=i['fixture']['status']['short'],
                           status_elapsed=i['fixture']['status']['elapsed'],
                           league_id=i['league']['id'],
                           league_name=i['league']['name'],
                           league_country=i['league']['country'],
                           league_season=i['league']['season'],
                           league_round=i['league']['round'],
                           teams_home_id=i['teams']['home']['id'],
                           teams_home_name=i['teams']['home']['name'],
                           teams_home_winner=i['teams']['away']['winner'],
                           teams_away_id=i['teams']['away']['id'],
                           teams_away_name=i['teams']['away']['name'],
                           teams_away_winner=i['teams']['away']['winner'],
                           goal_home=i['goals']['home'],
                           goals_away=i['goals']['away'],
                           scores_halftime_home=i['score']['halftime']['home'],
                           scores_halftime_away=i['score']['halftime']['away'],
                           scores_fulltime_home=i['score']['fulltime']['home'],
                           scores_fulltime_away=i['score']['fulltime']['away'],
                           scores_extratime_home=i['score']['extratime']['home'],
                           scores_extratime_away=i['score']['extratime']['away'],
                           scores_penalty_home=i['score']['penalty']['home'],
                           scores_penalty_away=i['score']['penalty']['away']
                           )
        db.session.add(new_user)
        db.session.commit()

# Closing file
f.close()

# If you wanted to see all the record thorugh loop
# just put the below lines inside the loop


# print("Fixture_id", i['fixture']['id'])
# print("Fixture_referee", i['fixture']['referee'])
# print("Fixture_timezone", i['fixture']['timezone'])
# print("Fixture_date", i['fixture']['date'])
# print("Fixture_timestamp", i['fixture']['timestamp'])
# print("Fixture_periods_first", i['fixture']['periods']['first'])
# print("Fixture_periods_second", i['fixture']['periods']['second'])
# print("Fixture_venue_id", i['fixture']['venue']['id'])
# print("Fixture_venue_name", i['fixture']['venue']['name'])
# print("Fixture_venue_city", i['fixture']['venue']['city'])
# print("Fixture_status_long", i['fixture']['status']['long'])
# print("Fixture_status_short", i['fixture']['status']['short'])
# print("Fixture_status_elapsed", i['fixture']['status']['elapsed'])
# print("league_id", i['league']['id'])
# print("league_name", i['league']['name'])
# print("league_country", i['league']['country'])
# print("league_season", i['league']['season'])
# print("league_round", i['league']['round'])
# print("teams_home_id", i['teams']['home']['id'])
# print("teams_home_name", i['teams']['home']['name'])
# print("teams_home-winner", i['teams']['home']['winner'])
# print("teams_away_id", i['teams']['away']['id'])
# print("teams_away_name", i['teams']['away']['name'])
# print("teams_away_winner", i['teams']['away']['winner'])
# print("goals_home", i['goals']['home'])
# print("goals_away", i['goals']['away'])
# print("score_halftime_home", i['score']['halftime']['home'])
# print("score_halftime_away", i['score']['halftime']['away'])
# print("score_fulltime_home", i['score']['fulltime']['home'])
# print("score_fulltime_away", i['score']['fulltime']['away'])
# print("score_extratime_home", i['score']['extratime']['home'])
# print("score_extratime_away", i['score']['extratime']['away'])
# print("score_penalty_home", i['score']['penalty']['home'])
# print("score_penalty_away", i['score']['penalty']['away'])
