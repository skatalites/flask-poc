# Flask Login POC

A simple login API built with Flask, following a layered architecture (routes → service → repository). Built as a learning project for a Java backend engineer picking up Python/Flask.

## Features

- `POST /login` — authenticate with username and password
- Passwords are hashed (never stored in plain text)
- Request validation with Pydantic
- In-memory "database" (no external DB needed to run it)

## Project Structure

```
flask-cru-api/
├── app/
│   ├── __init__.py        # application factory (create_app)
│   └── auth/
│       ├── __init__.py
│       ├── models.py       # User entity
│       ├── database.py     # in-memory storage + seed data
│       ├── repository.py   # data access layer
│       ├── service.py      # business logic (auth, password hashing)
│       ├── schemas.py      # request validation (Pydantic)
│       └── routes.py       # /login endpoint (Blueprint)
├── run.py                  # entry point
├── pyproject.toml
└── uv.lock
```

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (package manager)

## Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/skatalites/flask-poc.git
cd flask-poc
uv sync
```

## Running the app

```bash
uv run run.py
```

The API will start on `http://localhost:5000`.

## Testing the login endpoint

There's a seeded test user: `jose` / `secreto123`

```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "jose", "password": "secreto123"}'
```

Expected response (200):

```json
{
  "message": "Login exitoso",
  "username": "jose"
}
```

Wrong credentials return `401 Unauthorized`. Missing or invalid fields return `400 Bad Request`.

## Tech Stack

- **Flask** — web framework
- **Werkzeug** — password hashing (`generate_password_hash` / `check_password_hash`)
- **Pydantic** — request validation
- **uv** — dependency management

## Notes

This is a learning/POC project. The "database" is an in-memory Python dict — data resets every time the app restarts. A real database (e.g. SQLite + SQLAlchemy) would replace `database.py` without needing to change the service or routes layers.