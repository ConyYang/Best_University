from bs4 import BeautifulSoup
import pickle
import bs4


with open("ScrapyGoodUni/html.pkl", 'rb') as handle:
    html = pickle.load(handle)

soup = BeautifulSoup(html, "html.parser")
data = soup.find("tbody").children


def print_data():
    for tr in data:
        print(tr)


info = []
for tr in data:
    if isinstance(tr, bs4.element.Tag):
        tds = tr.find_all('td')
        print(tds[0].string, tds[1].string, tds[4].string)
        print("\n")

