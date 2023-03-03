from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com")
yc_page = response.text

soup = BeautifulSoup(yc_page, 'html.parser')

news = soup.select(selector='.titleline a')
scores = soup.select(selector='.subline .score')

content = []
for i in news:
    text = i.getText()
    content.append(text)

points = []
for i in scores:
    pt = i.getText().split(' ')[0]
    points.append(pt)
final = []
for i in range(len(scores)):
    ...
    ct = content[i]
    sc = points[i]
    final.append((ct, sc))

print(final)
# with open('website.html', encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)

# all_anchor_tags = soup.find_all(name='a')
# # print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get('href'))

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

# company_url = soup.select_one(selector='p a')

# name = soup.select_one(selector='#name')
# print(company_url)
# print(name)

# heading = soup.select('.heading')
# print(heading)
# soup.find
