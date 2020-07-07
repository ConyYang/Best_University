from bs4 import BeautifulSoup
import pickle
import json

with open("html.pkl", "rb") as handle:
    html = pickle.load(handle)

soup = BeautifulSoup(html, "html.parser")

div = soup.find('body').div

# find tag <a> and class = "link block"
a = soup.find_all('a', 'link block')

# <img alt="新手入门指南之玩转实验楼" class="cover-image" data-v-ab8793cc=""
# src="https://dn-simplecloud.shiyanlou.com/courses/uid214893-20200325-1585103411810?imageView2/2/h/150/q/100"/>
# i.get('href')
# href="/courses/63"
# i.find('div', 'course-cover relative')

href_list = []
div_list_name = []
for i in a:
    href_list.append("https://www.shiyanlou.com" + i.get('href'))
    div_list_name.append(i.find('div', 'course-cover relative'))

img_list = []
for img in div_list_name:
    img_list.append(img.find('img'))

alt_list = []
for alt in img_list:
    alt_list.append(alt.get('alt'))

info_dict = {}
for i in range(len(alt_list)):
    courseID = 'course' + str(i)
    info_dict[courseID] = {"name": alt_list[i],"course_link":href_list[i]}


with open("infoDict.json", 'w', encoding='utf-8') as outfile:
    json.dump(info_dict, outfile, indent=4, ensure_ascii=False)
