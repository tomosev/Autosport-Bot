import requests
import datetime
import os
from dotenv import load_dotenv
import config


load_dotenv()
year = datetime.datetime.now().year

# function to stop repeated json code.
# Fun fact the code used to be 5000 letters long.
def api_request(url):
    r = requests.get(url)
    json = r.json()
    return json


def f1_driver_standings():
    data = api_request(url="http://ergast.com/api/f1/current/driverStandings.json")
    return data


def f1_team_standings():
    data = api_request(url="http://ergast.com/api/f1/current/constructorStandings.json")
    return data


def f1_race_schedule():
    data = api_request(url="http://ergast.com/api/f1/current.json")
    return data


def f1_latest_results():
    data = api_request(url="http://ergast.com/api/f1/current/last/results.json")
    return data


def f1_driver_info(name):
    data = api_request(url=f"http://ergast.com/api/f1/drivers/{name}.json")
    return data


def f1_drivers_all():
    data = api_request(url=f"http://ergast.com/api/f1/{year}/drivers/.json")
    return data


def f1_team_info(name):
    data = api_request(url=f"http://ergast.com/api/f1/constructors/{name}.json")
    return data


def f1_team_all():
    data = api_request(url=f"http://ergast.com/api/f1/{year}/constructors.json")
    return data


def f1_latest_qualifying():
    round_data = f1_latest_results()
    round = round_data["MRData"]["RaceTable"]["round"]
    data = api_request(url=f"http://ergast.com/api/f1/{year}/{round}/qualifying.json")
    return data


def f1_random_gif():
    parameters = {"api_key": config.BOT_GIF_KEY, "tag": "formula 1", "rating": "r"}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    r = requests.get(
        "https://api.giphy.com/v1/gifs/random", params=parameters, headers=headers
    )
    json_data = r.json()
    return json_data