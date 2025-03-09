import sqlite3
import requests
from bs4 import BeautifulSoup
import csv

# Define database
DB_NAME = "jobs.db"

# Function to create database
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(job_title, company, location)
        )
    ''')
    conn.commit()
    conn.close()

# Function to scrape jobs
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    job_listings = []
    jobs = soup.find_all("div", class_="card-content")

    for job in jobs:
        job_title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="content").text.strip()
        application_link = job.find("a", text="Apply").get("href")

        job_listings.append((job_title, company, location, description, application_link))
    
    return job_listings

# Function to insert jobs into the database
def save_jobs_to_db(jobs):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute('''
            INSERT OR IGNORE INTO jobs (job_title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
        ''', job)

    conn.commit()
    conn.close()

# Function to filter jobs
def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = "SELECT job_title, company, location, description, application_link FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location = ?"
        params.append(location)
    
    if company:
        query += " AND company = ?"
        params.append(company)

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return results

# Function to export to CSV
def export_to_csv(filename, jobs):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)

# Run the functions
create_database()
jobs = scrape_jobs()
save_jobs_to_db(jobs)

# Example: Export jobs in a specific location to CSV
filtered_jobs = filter_jobs(location="Remote")
export_to_csv("remote_jobs.csv", filtered_jobs)
print("Filtered jobs exported to CSV.")
