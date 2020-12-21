import requests
from bs4 import BeautifulSoup

# Set the url of the news site
load_url = "https://www.itmedia.co.jp/news/subtop/aiplus/"

# Scripting news site article urls
def news_data_url():
    html = requests.get(load_url)
    soup = BeautifulSoup(html.text, "html.parser")
    found_list = soup.find_all("div", class_="colBoxIcon")
    url_list = []
    for url in found_list:
        print(url.a["href"])
        url_list.append(url.a["href"])
    return url_list

# Scraping article titles on news sites
def news_data_title():
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, 'html.parser')
    found_list = soup.find_all("div", class_="colBoxTitle")
    text_list = []
    for texts in found_list:
        print(texts.get_text())
        text_list.append(texts.get_text())
    return text_list














