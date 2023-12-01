from bs4 import BeautifulSoup
import requests

response  = requests.get("https://news.ycombinator.com/news")
website = response.text

soup = BeautifulSoup(website, "html.parser")
#get the <span> first and then the nested <a> tag
title_span = soup.find_all('span', class_='titleline')

article_titles = []
article_links = []
for article in title_span:
  a_element = article.find('a') if title_span else None
  #getting separate components and add them to list
  article_title = a_element.getText()
  article_titles.append(article_title)
  article_link = a_element["href"]
  article_links.append(article_link)


# #points are in a different span
points_span = soup.find_all("span", class_="score")
#list comprehension (substitute for "for loop") || got rid of the "points" text and converted number to int
points = [int(point.get_text().split()[0]) for point in points_span]

# print(article_titles)
# print(article_links)
# print(points)
most_upvotes_index = points.index(max(points))
print(article_titles[most_upvotes_index])
print(article_links[most_upvotes_index])
print(points[most_upvotes_index])