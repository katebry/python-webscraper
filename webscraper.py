import requests
from bs4 import BeautifulSoup

URL = 'https://uk.indeed.com/jobs?q=process+engineer&l=Manchester,+Greater+Manchester&from=mobRdr&utm_source=%2Fm%2F&utm_medium=redir&utm_campaign=dt'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')

job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

for job_elem in job_elems:
    title_elem = job_elem.find('a', class_='jobtitle')
    salary_elem = job_elem.find('span', class_='salaryText')
    print(title_elem, salary_elem, end='\n'*4)
