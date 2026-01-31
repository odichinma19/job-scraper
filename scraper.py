import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    data = []

    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()

        data.append([title, company, location])

    return data


def save_to_csv(data):
    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location"])
        writer.writerows(data)

    print("Saved to jobs.csv")


if __name__ == "__main__":
    jobs = scrape_jobs()
    save_to_csv(jobs)
    print("Scraping complete!")
