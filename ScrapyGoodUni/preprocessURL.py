import requests
r = requests.get("http://www.zuihaodaxue.com/ARWU2019.html")
import pickle


def check(request):
    print(request.status_code)
    print(request.encoding)
    if request.encoding != "utf-8":
        request.encoding = request.apparent_encoding
    print(request.encoding)
    return request


r = check(r)
html = r.text

with open("html.pkl", 'wb') as handle:
    pickle.dump(html, handle)

