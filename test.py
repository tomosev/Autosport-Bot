import data.f1_data as f1data
from bs4 import BeautifulSoup
import time


n = True

saved_guid = open("id.txt", "r").read()


def getrsslatest():
    while n == True:
        data = f1data.autosportf1()
        guid = data.find("guid").string
        title = data.find_all("title")[2].string
        desc = data.find_all("description")[1].string
        link = data.find_all("link")[3].string
        if guid in saved_guid:
            pass
        else:
            with open("id.txt", "w") as id:
                id.write(guid)
                id.close()
        time.sleep(100)


getrsslatest()
