from bs4 import BeautifulSoup
import requests

# HACKER NEWS
# response = requests.get("https://news.ycombinator.com")
# yc_page = response.text

# soup = BeautifulSoup(yc_page, 'html.parser')

# articles = soup.find_all(name="span", class_="titleline")

# article_texts = []
# article_links = []

# for i in articles:
#     text = i.get_text().split('(')[0]
#     article_texts.append(text)
#     link = i.get_text().split('(')[1]
#     article_links.append(link)

# article_upvotes = [int(i.getText().split(' ')[0])
#                    for i in soup.select(selector='.subline .score')]

# max_num = max(article_upvotes)
# max_index = article_upvotes.index(max_num)

# print(article_texts[max_index])
# print(article_links[max_index].split(')')[0])


# 100 movies

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

empire_page = response.text
soup = BeautifulSoup(empire_page, 'html.parser')
movies_titles = soup.find_all(name="h3", class_="title")
movies = movies_titles[::-1]
top_movies = [i.getText() for i in movies]
print(top_movies)

with open('movies.txt', mode='w', encoding="utf-8") as file:
    for i in top_movies:
        file.write(f'{i}\n')


# news = soup.select(selector='.titleline ')
# scores = soup.select(selector='.subline .score')


# print(article_upvotes)
# content = []
# for i in news:
#     text = i.getText()
#     content.append(text)

# print(content)


# print(final)
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
