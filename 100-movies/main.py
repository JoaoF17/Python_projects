from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = response.text

soup = BeautifulSoup(website, "html.parser")

#get movie titles
titles = soup.find_all("h3", class_="title")
#loop thorugh the movie tags and add them to a list and reverse that list to go from 1 to 100
titles_list = [title.getText() for title in titles]
titles_list_reverse = titles_list[::-1]

#create a .txt file
top_100_movies = "top_100_movies.txt"

with open(top_100_movies, "w") as file:
  for movie in titles_list_reverse:
    file.write(movie + "\n")
