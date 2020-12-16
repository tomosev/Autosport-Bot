import requests
import datetime
from bs4 import BeautifulSoup
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
    return api_request(url="http://ergast.com/api/f1/current/driverStandings.json")


def f1_team_standings():
    return api_request(url="http://ergast.com/api/f1/current/constructorStandings.json")


def f1_race_schedule():
    return api_request(url="http://ergast.com/api/f1/current.json")


def f1_latest_results():
    return api_request(url="http://ergast.com/api/f1/current/last/results.json")


def f1_driver_info(name):
    return api_request(url=f"http://ergast.com/api/f1/drivers/{name}.json")


def f1_drivers_all():
    return api_request(url=f"http://ergast.com/api/f1/{year}/drivers/.json")


def f1_team_info(name):
    return api_request(url=f"http://ergast.com/api/f1/constructors/{name}.json")


def f1_team_all():
    return api_request(url=f"http://ergast.com/api/f1/{year}/constructors.json")


def f1_latest_qualifying():
    round_data = f1_latest_results()
    round = round_data["MRData"]["RaceTable"]["round"]
    return api_request(url=f"http://ergast.com/api/f1/{year}/{round}/qualifying.json")


def f1_random_gif():
    parameters = {"api_key": config.BOT_GIF_KEY, "tag": "formula 1", "rating": "r"}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    r = requests.get(
        "https://api.giphy.com/v1/gifs/random", params=parameters, headers=headers
    )
    return r.json()


def autosportf1():
    r = requests.get("https://www.autosport.com/rss/feed/f1")
    return BeautifulSoup(r.content, "xml")