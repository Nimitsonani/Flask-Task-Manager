# TaskFlow - Flask Task Manager

A Task web application built with Flask, featuring user authentication, task management, SQLAlchemy ORM, and a responsive Bootstrap UI.

---

## Project Overview

TaskFlow is a simple Task Manager web application built with Flask.  
It includes user authentication and allows each user to manage their own tasks.

If a user is not logged in, tasks are stored temporarily in memory.  
Refreshing the page will clear those tasks.

If a user is logged in, tasks are stored in a relational SQLite database and are linked to that specific user. This allows tasks to persist even after refreshing the page or logging out and back in.

---

## Features

- User registration and login
- Password hashing using Werkzeug
- Session management with Flask-Login
- Create and delete tasks
- Mark tasks as completed
- Each user sees only their own tasks
- Flash messages for feedback
- SQLite database using SQLAlchemy

---

## Tech Stack

- Flask
- Flask-Login
- Flask-WTF
- Flask-Bootstrap5
- SQLAlchemy
- SQLite
- Bootstrap 5
- Jinja2

---

## Project Structure

```
main.py            # Application routes and logic
forms.py           # Form definitions
templates/         # HTML templates
static/            # CSS and JavaScript files
```

---

## Environment Variables

This project uses environment variables for configuration.

Create a `.env` file in the root directory:

```
SECRET_KEY=your_secret_key_here
DB_URI=sqlite:///todolist.db
```

- SECRET_KEY: used for session security
- DB_URI: database connection string

---

## Setup

1. Install dependencies

```
pip install -r requirements.txt
```

2. Create a `.env` file and add the required variables

3. Run the application

```
python main.py
```

---

## Screenshot

<img width="1920" height="890" alt="image" src="https://github.com/user-attachments/assets/e6281811-8186-45e8-983b-6798c7235f96" />
