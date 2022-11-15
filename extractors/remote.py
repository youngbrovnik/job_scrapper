from bs4 import BeautifulSoup
import requests

def extract_remote_jobs(term):
  base_url = "https://remoteok.com"
  url = f"{base_url}/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    results = []
    # write your ✨magical✨ code here
    jobs = soup.find_all('tr', class_ = 'job')
    for job_section in jobs:
      link = base_url + job_section['data-url']
      company = job_section.find('h3', itemprop="name")
      position = job_section.find('h2', itemprop="title")
      locations = job_section.find_all('div', class_="location")
      location_edit = []
      for location in locations:
        location_edit.append(location.string)
      
      job_data = {
        'link': f'{link}',
        'company': company.string.replace("\n", ""),
        'position': position.string.replace("\n", ""),
        'location' : location_edit
      }
      results.append(job_data)
    return results
  
  else:
    print("Can't get jobs.")
  