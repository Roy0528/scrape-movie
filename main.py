import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

all_movies = soup.select(selector=".article-title-description__text .title")

movie_titles = [movie.getText() for movie in all_movies]
movie_titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in movie_titles:
        title = title.replace(":", ")")
        file.write(title + "\n")
