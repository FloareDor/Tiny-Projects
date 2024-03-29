from bs4 import BeautifulSoup
import requests as req
html_text = req.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    company = job.find('h3', class_ = 'joblist-comp-name').text.strip()
    skills = job.find('span', class_ = 'srp-skills').text.strip().replace(' ', '')
    published_date = job.find('span', class_ = 'sim-posted').text.strip()
    print(f'''Company Name: {company}
Required Skills: {skills}''')
    print(f"{published_date}\n")
