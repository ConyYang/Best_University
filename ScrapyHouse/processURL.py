
import requests
import pickle
url = "https://bj.lianjia.com/zufang/"
response = requests.get(url)
print(response)
print(response.encoding)
html = response.text

with open('html.pkl', 'wb') as handle:
    pickle.dump(html, handle)