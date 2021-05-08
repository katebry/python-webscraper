import requests

URL = 'https://www.monster.com/jobs/search/?q=Process-Engineer&where=UK'
page = requests.get(URL)
