import bs4
import requests
from lxml import etree

url = 'https://plain-wildflower-2fe4.inf.workers.dev/-----https://www.meizitu.com/'
headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    'Reference':'https://www.meizitu.com/tag/ugirls'
}
r = requests.get(url, headers = headers)
print(r.status_code)
html = etree.HTML(r.text)
name_list = html.xpath('//img[@class="lazy"]/@alt')

image_list = html.xpath('//img[@class="lazy"]/@data-original')

for name, img in zip(name_list, image_list):
    image = requests.get(url=img, headers=headers)
    file_name = 'img/' + name + '.jpg'
    print("Now saving ..." + file_name)
    with open(file_name, 'wb') as file:
        file.write(image.content)