import pickle
from lxml import etree
import pyttsx3

with open('html.pkl', 'rb') as handle:
    html= pickle.load(handle)


data = etree.HTML(html)
weather_text = data.xpath('//dl[@class="weather_info"]//text()')

content = ''
for text in weather_text:
    content += text


weather = pyttsx3.init()

weather.say()