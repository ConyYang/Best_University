
import requests

import pickle

weather_url = 'https://www.tianqi.com/chongqing/'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
response = requests.get(url=weather_url, headers=header)
html = response.text

with open('html.pkl', 'wb') as handle:
    pickle.dump(html, handle)