
JobPulseNotifier
----------------------------------------
### Ted Staros

![Flask](https://img.shields.io/badge/Flask-v3.0.3-white)
![Python](https://img.shields.io/badge/Python-v3.12.3-blue)
![Werkzeug](https://img.shields.io/badge/Werkzeug-v3.0.3-pink)
---
Job Pulse Notifier is a job alert app. Users provide the app with the names of the job postings they are looking for and the career webpages they want to monitor. The app will scrape these career pages and send users an email notification when a new job posting that fits their criteria becomes available.

## Prerequisites
- Python 3.12.3
- pip (Python package installer)
## Setup
* Clone or Fork this repository
    * `git clone <repository-url>`
    * `cd job_pulse_notifier`
* Create and activateyour virtual environment:
    * `python3 -m venv .venv`
    * `source .venv/bin/activate`
    * Alternatively, if you're using Windows, it would be:
    * `.\path\to\your\venv\Scripts\activate`
* Install all required packages:
    * `pip install -r requirements.txt`
## To run the project
* To run the application:
    * `python3 job_pulse/app.py`
* To Run the test suite:
    * `pytest`
