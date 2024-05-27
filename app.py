from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/scrape")
def scrape():
    jobs = scrape_news()
    return {"jobs" : jobs }

def scrape_news():
    print ("scrape news is called")
    url = "https://www.usta.com/en/home/about-usta/jobs---human-resources/middlestates/employment-opportunities.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = []
    for job in soup.find_all("h3", class_="headline"):
        jobs.append(job.text)
    return jobs

if __name__ == "__main__":
 app.run(debug=True, use_reloader=False)

