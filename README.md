# ☁ CloudTask – Cloud Hosted Task Manager

Mini Project (Case Study) for Cloud Computing.

CloudTask is a simple task manager web application. Users can add tasks, mark them as completed and delete them.
The project is stored on GitHub and hosted on **AWS EC2** (cloud) as well as on a **local machine**.

## Tech Stack
- Python Flask (web framework)
- SQLite (database)
- Gunicorn (production server)
- AWS EC2 (cloud hosting)

## Features
- Add / complete / delete tasks
- Shows which host served the page (cloud server or local machine)
- REST API: `/api/tasks` returns tasks in JSON

## Run locally
```
pip install -r requirements.txt
python3 app.py
```
Open http://localhost:5000

## Deploy on AWS EC2 (Ubuntu)
```
git clone https://github.com/<username>/cloudtask.git
cd cloudtask
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
gunicorn -b 0.0.0.0:5000 app:app
```
Open http://<EC2-public-IP>:5000 (allow port 5000 in the security group)
