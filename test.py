import data.f1_data as f1data
from bs4 import BeautifulSoup
import time

saved_guid = []


n = 1


def getrsslatest():
    while n <= 1:
        with open("index.xml", "r") as f:
            contents = f.read()
        data = BeautifulSoup(contents, "lxml")
        # data = f1data.autosportf1()
        guid = data.find("guid").string
        title = data.find_all("title")[2].string
        desc = data.find_all("description")[1].string
        link = data.find_all("link")[3].string
        if guid in saved_guid:
            pass
        else:
            list.clear(saved_guid)
            saved_guid.append(guid)
        print(saved_guid)
        time.sleep(1)


# Able to store the savedguid inside a list, better if I had a database for it all, hmmmm

getrsslatest()