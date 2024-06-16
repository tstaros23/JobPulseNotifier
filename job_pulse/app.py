from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
from job_pulse.robots import check_robots_txt  # Import the function from the job_pulse module

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/scrape")
def scrape():
    jobs = scrape_jobs()
    return jsonify({"jobs" : jobs})

def scrape_jobs():
    url = "https://www.usta.com/en/home/about-usta/jobs---human-resources/middlestates/employment-opportunities.html"
    if not check_robots_txt(url):
        return []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    
    container = soup.find('div', attrs = {'id': 'text-353cc9e8aa'} )
    job_listings = container.find_all('h5')
    
    jobs = []
    for job in job_listings:
        jobs.append(job.get_text(strip=True))
    return jobs

if __name__ == "__main__":
 app.run(debug=True, use_reloader=False)

