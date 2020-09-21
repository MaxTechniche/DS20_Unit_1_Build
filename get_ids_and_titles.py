from bs4 import BeautifulSoup
import requests

t_url = "https://www.imdb.com/chart/top"
imdb = "https://www.imdb.com"

source = requests.get(t_url).text

soup = BeautifulSoup(source, 'html.parser')

movies_page = soup.find('tbody', class_='lister-list')
movie_links = movies_page.find_all('a')
movie_years = [x.text for x in movies_page.find_all('span', class_='secondaryInfo')]

movie_titles = {title['href'][9:-1]:title.text for title in movie_links}

with open('top250imdblist.csv', 'w') as file:
    file.write('ID,Title_Name,Year\n')
    for id_, name, year in zip(movie_titles.keys(), movie_titles.values(), movie_years):
        file.write(id_ + ',' + '"' + name + '",' + year[1:-1] + '\n')

