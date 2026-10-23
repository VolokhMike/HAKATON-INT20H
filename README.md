# HAKATON INT20H: Quest Platform

An educational web platform where users sign up, verify their e-mail and work through quests. Built with Flask during the INT20H hackathon.

## Context

The project was built for **INT20H** (February–March 2025), one of the largest student IT hackathons in Ukraine, organised by **BEST Kyiv**.
Our team of four (2 frontend, 2 backend developers) **passed the qualification round and reached the final**.

**My role (Mykhailo Volokh): Team Lead & Backend Developer.** I led the team and wrote the entire backend.

## Features

- **Sign-up and login** with Flask-Login session handling and logout
- **E-mail verification**: a 6-digit code is sent over SMTP (Gmail) after sign-up, and login is blocked until the address is verified
- **User profiles**: view your own or another user's profile, and edit your username, e-mail, profile photo URL and description. Each profile also stores points.
- **Quests**: create quests (name, description, points) and list existing quests on the quest page and the profile
- **Admin route**: a hardcoded admin account is sent to a separate admin page (the template is still a placeholder)
- **Automatic database setup**: SQLite tables (`users`, `quests`, `profile`) are created on startup

## Tech Stack

| Layer    | Technology                                     |
|----------|------------------------------------------------|
| Backend  | Python 3, Flask, Flask-Login                   |
| Database | SQLite (via the built-in `sqlite3` module)     |
| Templates| Jinja2 (Flask)                                 |
| Frontend | HTML, CSS, JavaScript, Font Awesome (CDN)      |
| E-mail   | `smtplib` (Gmail SMTP, STARTTLS)               |

## Project Structure

```
HAKATON-INT20H/
├── main.py               # entry point, starts the dev server on port 30000
├── connection.py         # SQLite connection + table creation
├── requirements.txt
├── .env.example          # template for environment variables
└── app/
    ├── __init__.py       # Flask app, LoginManager, config
    ├── models/
    │   └── user.py       # User model (Flask-Login UserMixin)
    ├── routes/
    │   ├── auth.py       # signup, login, logout, e-mail verification
    │   ├── profile.py    # view / edit profile
    │   └── quests.py     # start page, menu, admin page, quests
    ├── templates/        # Jinja2 templates (login, signup, verification, menu,
    │                     #   profile, edit_profile, add_quests, admin_page, base)
    └── static/
        ├── css/style.css
        ├── js/api.js
        └── photos/
```

## Getting Started

**Requirements:** Python 3

```bash
git clone https://github.com/VolokhMike/HAKATON-INT20H.git
cd HAKATON-INT20H

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env            # then fill in the values
python main.py
```

Then open **http://127.0.0.1:30000** in your browser.

The SQLite database `users.db` is created automatically on first start.

### Configuration (`.env`)

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Flask session secret |
| `MAIL_USERNAME` | Gmail address that sends verification codes |
| `MAIL_APP_PASSWORD` | Gmail app password for that address |
| `ADMIN_USERNAME`, `ADMIN_PASSWORD` | Account that is shown the admin page |
| `FLASK_DEBUG` | `1` enables Flask debug mode (local development only) |
