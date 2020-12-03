from bs4 import BeautifulSoup
import requests
import json
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()


# year = datetime.now().year
# number = year
# number2 = "2"

# roundParam = {"year": number, "round": number2}
# qualifyParam = {"year": number, "round": number2}
# raceParam = {"year": number, "round": number2}


class webCollectData:
    # def webScrapeData(self):
    #     web_url = os.environ.get("WEB_URL")
    #     r = requests.get(web_url)
    #     soup = BeautifulSoup(r.content, "html.parser")
    #     script = soup.find_all("script")[6].string.strip()[11:]
    #     self.json_data = json.loads(script)
    #     return self.json_data

    def apiRaceSchedule(self):
        api_url = "http://ergast.com/api/f1/current.json"
        r = requests.get(api_url)
        self.json_data = r.json()
        return self.json_data

    def apiDriverInfo(self, name):
        api_url = f"http://ergast.com/api/f1/drivers/{name}.json"
        r = requests.get(api_url)
        self.json_data = r.json()
        return self.json_data

    def apiDriversAll(self, year):
        api_url = f"http://ergast.com/api/f1/{year}/drivers/.json"
        r = requests.get(api_url)
        self.json_data = r.json()
        return self.json_data

    def apiConstructorInfo(self, name):
        api_url = f"http://ergast.com/api/f1/constructors/{name}.json"
        r = requests.get(api_url)
        self.json_data = r.json()
        return self.json_data

    def apiConstructorAll(self, year):
        api_url = f"http://ergast.com/api/f1/{year}/constructors.json"
        r = requests.get(api_url)
        self.json_data = r.json()
        return self.json_data


# Import time to add sleep functionality to stop mass requests
