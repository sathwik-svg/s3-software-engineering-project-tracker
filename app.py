from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

database_url = os.environ.get("DATABASE_URL", "sqlite:///projects.db")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default="Planning")
    priority = db.Column(db.String(50), default="Medium")
    deadline = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    tasks = db.relationship(
        "Task",
        backref="project",
        lazy=True,
        cascade="all, delete-orphan"
    )


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(50), default="Todo")
    priority = db.Column(db.String(50), default="Medium")
    project_id = db.Column(
        db.Integer,
        db.ForeignKey("project.id"),
        nullable=False
    )


@app.route("/")
def index():
    projects = Project.query.order_by(Project.created_at.desc()).all()

    total_projects = Project.query.count()
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter_by(status="Completed").count()

    progress = 0
    if total_tasks:
        progress = round((completed_tasks / total_tasks) * 100)

    return render_template(
        "index.html",
        projects=projects,
        total_projects=total_projects,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        progress=progress
    )


@app.route("/projects")
def projects():
    return render_template(
        "projects.html",
        projects=Project.query.order_by(Project.created_at.desc()).all()
    )


@app.route("/projects/add", methods=["POST"])
def add_project():
    project = Project(
        name=request.form["name"],
        description=request.form["description"],
        status=request.form.get("status", "Planning"),
        priority=request.form.get("priority", "Medium"),
        deadline=request.form.get("deadline")
    )

    db.session.add(project)
    db.session.commit()

    return redirect(url_for("projects"))


@app.route("/projects/<int:project_id>")
def project(project_id):
    project_data = db.get_or_404(Project, project_id)

    return render_template(
        "project.html",
        project=project_data
    )


@app.route("/projects/<int:project_id>/tasks/add", methods=["POST"])
def add_task(project_id):
    project_data = db.get_or_404(Project, project_id)

    task = Task(
        title=request.form["title"],
        status=request.form.get("status", "Todo"),
        priority=request.form.get("priority", "Medium"),
        project_id=project_data.id
    )

    db.session.add(task)
    db.session.commit()

    return redirect(url_for("project", project_id=project_id))


@app.route("/tasks")
def tasks():
    return render_template(
        "tasks.html",
        tasks=Task.query.all()
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "S3 Software Engineering Project Tracker"
    })


@app.route("/api/projects")
def api_projects():
    projects = Project.query.all()

    return jsonify([
        {
            "id": project.id,
            "name": project.name,
            "status": project.status,
            "priority": project.priority
        }
        for project in projects
    ])


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
