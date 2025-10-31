import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    response = requests.get("https://www.juniors.ro/jobs")
    if response.status_code == 200:
        html_doc = response.text
    else:
        print("Bad request")
        exit(1)
    
    soup = BeautifulSoup(html_doc, "html.parser")

    jobs_html = soup.find_all("li", "job")

    jobs = [(job.find("div", "job_header_title").h3.get_text().strip(),
             job.find("ul", "job_requirements").li.get_text().split(':')[1].strip(),
             job.find("div", "job_header_title").strong.get_text().split('|')[0].strip(),
             [tech.string for tech in job.find("ul", "job_tags").find_all("a")],
             job.find("div", "job_header_title").strong.get_text().split('|')[1].strip()) for job in jobs_html]

    jobs = jobs[:7]

    for job in jobs:
        print(f"Job title: {job[0]}")
        print(f"Company: {job[1]}")
        print(f"Location: {job[2]}")
        print(f"Technologies: {", ".join(job[3])}")
        print(f"Post date: {job[4]}")
        print()