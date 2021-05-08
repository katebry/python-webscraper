import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Process+Engineer&where=UK'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)
