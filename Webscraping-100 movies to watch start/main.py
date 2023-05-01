import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

print(soup.prettify())

# all movies names ar einside the h3 tag and class title, we are scarping it out the text out of it
all_movies = soup.find_all(name='h3', class_='title')
print(all_movies)

# all movies is a list for we cant use gettext , need to use for loop
# movie_titiles = [item for movie in all_movies]

movie_titles = [movie.getText() for movie in all_movies]
print(movie_titles)

# now need to slice  aND REVERSE

# slice(start:stop:end)

# for n in range(len(movie_titles)-1, 0, -1):
#     #print(n)
#     print(movie_titles[n])
movies = movie_titles[::-1]
print(movies)
# with open("movies.txt", mode='w')as file:
#     for movie in movies:
#         file.write(f"{movie}\n")
