import pickle
from bs4 import BeautifulSoup
import json
import re

with open("html.pkl", 'rb') as handle:
    html = pickle.load(handle)
soup = BeautifulSoup(html, 'html.parser')


url = "https://bj.lianjia.com/"
links_div = soup.find_all('p', class_="content__list--item--title twoline")


house_urls = []  #House Url
for link in links_div:
    mylink = url + link.a.get('href')
    house_urls.append(mylink)

house_name = []
for link in links_div:
    content = link.a.contents[0]
    content = re.sub("\A\s+", "",content)
    content = re.sub("\s+\Z","", content)
    house_name.append(content)

house_page = {}
for i in range(len(house_urls)):
    houseID = "House" + str(i)
    house_page[houseID] = {"House Name": house_name[i], "House Url": house_urls[i]}
print(house_page)

with open("HouseDict.json", 'w', encoding='utf-8') as outfile:
    json.dump(house_page, outfile, indent=4, ensure_ascii=False)