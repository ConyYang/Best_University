import requests
import pickle

try:
    url = "https://www.shiyanlou.com/courses/"
    r = requests.get(url)
    print(r.raise_for_status)
    r.encoding = r.apparent_encoding
    html = r.text
    with open("html.pkl", 'wb') as handle:
        pickle.dump(html, handle)
    print(html)
except:
    print("Nothing detect")

