#This is a python webscraper to get postings from fake-python
#A tutorial from realpython website

import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)
counter = 1

#parse respsonse
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elements = results.find_all('div', class_='card-content')
python_jobs = []

for job in job_elements:
    python_jobs += job.find_all('h2', string= lambda text: 'python' in text.lower())

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
full_list = ''
for job_element in python_job_elements:
    title_element = job_element.find('h2', class_='title').text.strip()
    company_element = job_element.find('h3', class_='subtitle').text.strip()
    location_element =job_element.find('p', class_='location').text.strip()
    link = job_element.find_all('a')[1]['href'].strip()

    list = str(str(counter) + '.' + 'Job Title: ' + title_element +  '\nCompany: ' + company_element + '\nLocation: ' + location_element + '\nLink: ' + link + '\n\n')
    counter += 1
    full_list += list
with open('C:\\Users\\Dikio Daniel\\Desktop\\Scraper\\pythonjobs.txt', 'w') as file:
    file.write(full_list)

