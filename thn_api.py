import requests
from bs4 import BeautifulSoup
import json

with open("./config.json") as configfile:
    config = json.load(configfile)

def get_thn_data(optimal=False):

    # object/list of The Hacker New URLS
    THN_URLS = config["thn_urls"]

    URL = THN_URLS["base"]
    if optimal == False:
        URL = THN_URLS["maxd"]

    # Credit: https://realpython.com/beautiful-soup-web-scraper-python/
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    filtered_htmls = soup.find_all("div", class_="body-post clear")

    cdata = []
    for segment in filtered_htmls:

        line = str(segment).split("\n")

        # filter out article's url:
        url = line[1]
        url = url[url.find("https://"): url.find('\">')]

        # filter out article's title:
        title = line[5]
        title = title[title.find('<img alt=\"')+len('<img alt=\"'):title.find('\" loading=')]

        # filter out article's detail (some of it's detail):
        detail = line[11]
        detail = detail[detail.find('<div class="home-desc"> ')+len('<div class="home-desc"> '):detail.find('</div>')]

        cdata.append({"url": url, "title": title, "details": detail})
    
    return cdata

get_thn_data()