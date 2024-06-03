
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
##
Setup
* Clone or Fork this repository
* From the command line, create and activateyour virtual environment:
    
    * Run the command to activate your virtual environment. For example:
    * `source /path/to/your/venv/bin/activate`
    * Alternatively, if you're using Windows, it would be:
    * `.\path\to\your\venv\Scripts\activate`
    * Install all of the virtual environment requirements:
    * `pip install -r requirements.txt`
* To run the project from the command line:
    * `python3 app.py`
* To Run the test suite:
    * `pytest`
