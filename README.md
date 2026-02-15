# TaskFlow - Flask Task Manager

TaskFlow is a simple task management web application built with Flask.

It supports user authentication and persistent task storage using SQLAlchemy.  
The application is structured so that each user manages their own task list.

---

## What This Project Does

The application has two modes:

**1. Guest Mode (Not Logged In)**  
- Tasks are stored temporarily in memory.
- Refreshing the page clears the task list.
- No data is persisted.

**2. Authenticated Mode (Logged In)**  
- Tasks are stored in a relational SQLite database.
- Each task is linked to a specific user.
- Tasks remain saved even after logout and login.

This design demonstrates the difference between temporary in-memory storage and persistent database storage.

---

## How It Works

### Authentication

- Users register with a username and password.
- Passwords are hashed using Werkzeug.
- Flask-Login manages sessions.
- Protected routes ensure users can only access their own tasks.

---

### Task Management

Each task:

- Has a title
- Has a completion status (completed / not completed)
- Is linked to a specific user (via foreign key relationship)

Users can:

- Create tasks
- Mark tasks as completed
- Delete tasks

Each user only sees their own tasks.  
All queries are filtered by the currently authenticated user.

---

## Database Structure

The application uses SQLite with SQLAlchemy ORM.

There are two main models:

- **User**
- **Task**

Relationship:

- One user → many tasks

This ensures proper ownership and isolation of data between users.

---

## Screenshot

<img width="1920" height="890" alt="image" src="https://github.com/user-attachments/assets/e6281811-8186-45e8-983b-6798c7235f96" />

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
static/            # CSS and JS files
```

---

## Running Locally

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory:

```
SECRET_KEY=your_secret_key_here
DB_URI=sqlite:///todolist.db
```

- `SECRET_KEY` is required for session security.
- `DB_URI` defines the database connection.

3. Run the application:

```
python main.py
```

The database will be created automatically if it does not already exist.
