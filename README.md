# 🎓 S3 Software Engineering Project Tracker

A web-based **Software Engineering Project Tracker** developed as a college-level B.Tech CSE project.

The application helps students organize software projects, manage tasks, track priorities, monitor deadlines, and view overall project progress through a centralized dashboard.

## 🌐 Live Demo

**Application:**
https://s3-software-engineering-project-tracker.onrender.com/

**Health Check:**
https://s3-software-engineering-project-tracker.onrender.com/health

## 📌 Project Overview

Software development projects involve multiple tasks, deadlines, priorities, and progress stages. Managing these activities manually can become difficult.

This project provides a simple web-based solution for college students to:

* Create software projects
* Define project descriptions
* Set project status
* Set project priority
* Set deadlines
* Create project tasks
* Track task status
* Track task priority
* Monitor overall progress
* Access project information through a dashboard

## ✨ Features

### 📊 Dashboard

* Total project count
* Total task count
* Completed task count
* Overall task completion percentage
* Recent project overview

### 📁 Project Management

* Create new projects
* Project descriptions
* Project status
* Priority management
* Deadline tracking
* Individual project pages

### ✅ Task Management

* Create tasks for projects
* Todo status
* In Progress status
* Completed status
* Task priority
* View all tasks

### 🔌 API

The application provides simple API endpoints for application monitoring and project data.

```text
GET /health
GET /api/projects
```

## 🛠️ Technology Stack

| Technology       | Purpose                 |
| ---------------- | ----------------------- |
| Python           | Application programming |
| Flask            | Web framework           |
| Flask-SQLAlchemy | Database ORM            |
| SQLite           | Local database          |
| HTML5            | Web structure           |
| CSS3             | User interface          |
| JavaScript       | Frontend functionality  |
| Docker           | Containerization        |
| Git              | Version control         |
| GitHub           | Source-code hosting     |
| Render           | Cloud deployment        |
| Ubuntu Server    | Development environment |

## 🏗️ Architecture

```text
                 ┌──────────────────────┐
                 │      User Browser    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Render Web Service │
                 │      Docker          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      Flask App       │
                 │      Python          │
                 └──────────┬───────────┘
                            │
                   ┌────────┴────────┐
                   ▼                 ▼
              ┌─────────┐      ┌──────────┐
              │ SQLite  │      │ REST API │
              └─────────┘      └──────────┘
```

## 📂 Project Structure

```text
s3-software-engineering-project-tracker/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── render.yaml
├── .dockerignore
├── .gitignore
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── projects.html
│   ├── project.html
│   └── tasks.html
│
├── static/
│   └── css/
│       └── style.css
│
├── database/
│   └── schema.sql
│
└── tests/
    └── test_app.py
```

## 💻 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/s3-software-engineering-project-tracker.git
cd s3-software-engineering-project-tracker
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## 🐳 Running with Docker

Build the image:

```bash
docker build -t s3-software-engineering-project-tracker .
```

Run the container:

```bash
docker run -d \
  --name s3-project-tracker \
  -p 5000:5000 \
  s3-software-engineering-project-tracker
```

Test:

```bash
curl http://localhost:5000/health
```

## 🔍 API Endpoints

### Health Check

```http
GET /health
```

Example response:

```json
{
  "service": "S3 Software Engineering Project Tracker",
  "status": "healthy"
}
```

### Projects API

```http
GET /api/projects
```

Returns project information in JSON format.

## 🚀 Deployment

The application was developed on an **Ubuntu Server** and containerized using Docker.

Deployment pipeline:

```text
Ubuntu Server
      │
      ▼
     Git
      │
      ▼
    GitHub
      │
      ▼
    Render
      │
      ▼
 Docker Container
      │
      ▼
 Flask Application
      │
      ▼
 Live Web Application
```

## 🧪 Testing

The application can be tested using:

```bash
curl http://localhost:5000/health
```

API testing:

```bash
curl http://localhost:5000/api/projects
```

Browser testing:

```text
http://localhost:5000
```

## 🎯 Software Engineering Concepts Demonstrated

This project demonstrates several core Software Engineering concepts:

* Requirements analysis
* Modular application design
* Object-oriented data modeling
* Database design
* Web application development
* REST API development
* Version control
* Containerization
* Application testing
* Cloud deployment
* Documentation
* Project and task management

## 📚 Learning Outcomes

Through this project, the following practical skills were developed:

* Building a Flask web application
* Designing database models
* Creating dynamic web pages
* Creating REST endpoints
* Using Git and GitHub
* Creating Docker images
* Running containerized applications
* Deploying applications to Render
* Working with Linux/Ubuntu
* Writing technical documentation

## 🔮 Future Improvements

Possible future versions could include:

* PostgreSQL database
* User authentication
* Student/team member accounts
* Role-based access control
* Project search and filtering
* Task editing and deletion
* Progress charts
* Email notifications
* File attachments
* CI/CD with GitHub Actions
* Automated testing
* Production monitoring

## ⚠️ Database Note

The current college version uses SQLite for simplicity.

For a production deployment, the application should use a persistent database such as PostgreSQL rather than relying on local SQLite storage.

## 👨‍💻 Project Information

**Project:** S3-P5 Software Engineering Project Tracker
**Course:** B.Tech Computer Science & Engineering
**Category:** Software Engineering
**Environment:** Ubuntu Server
**Deployment:** Render
**Version Control:** GitHub

---

⭐ Built as part of a semester-wise B.Tech CSE software engineering project portfolio.
