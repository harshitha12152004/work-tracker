# Work Tracker App

A full-stack task management application with role-based views for Admins and Members, built with Django REST Framework and React.

## Features
- Task creation, updates, and status tracking via RESTful APIs
- Role-based views (Admin vs. Member) based on user role
- Task dependency logic with cycle detection (prevents circular task dependencies)
- Automatic task blocking/unblocking based on predecessor task progress
- React frontend consuming the backend APIs with live state updates across admin/member views

## Tech Stack
**Backend:** Python, Django, Django REST Framework
**Frontend:** React (Hooks, Component Architecture)
**Database:** MySQL

## Project Structure
```
work-tracker/
├── backend/
│   └── worktracker/    # Django project (manage.py, settings, work app)
└── frontend/            # React app
```

## Backend Setup
1. Navigate to the backend project folder and create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate   # Mac/Linux
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the same folder as `manage.py` with your own values:
   ```
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   DB_NAME=worktracker
   DB_USER=your_mysql_user
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306
   ```
4. Make sure MySQL is running locally and a database matching `DB_NAME` exists.
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## Frontend Setup
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```
3. Open the URL shown in the terminal (usually `http://localhost:5173`).

## Authentication
Login is handled via a custom endpoint that verifies user credentials and returns the user's `id` and `role`, which the frontend uses to route Admin vs. Member views.

> **Note:** This is currently a simplified auth flow (no token-based sessions yet). Planned improvement: migrate to JWT-based authentication using `djangorestframework-simplejwt` for stateless, token-based auth.

## Status
Running locally; not yet deployed.

## License
MIT
