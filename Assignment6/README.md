# 📸 PhotoAlbum — Production-Ready Django Photo Album Management System

A full-featured, production-ready Photo Album Management application built with Django, PostgreSQL, and Cloudinary.

## ✨ Features

- **Full CRUD Operations** — Create, Read, Update, and Delete albums and photos
- **Class-Based Views** — All views implemented using Django's generic CBVs
- **Role-Based Access Control (RBAC)** — Admin and Standard User roles with strict permissions
- **Cloud Storage** — All images stored on Cloudinary (no local media storage in production)
- **Responsive Design** — Modern dark-mode UI with glassmorphism aesthetics
- **Production-Ready** — Deployed on Render with PostgreSQL

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | Django 4.2 LTS |
| **Language** | Python 3.11 |
| **Database** | PostgreSQL (Render) / SQLite (local dev) |
| **Media Storage** | Cloudinary |
| **Static Files** | WhiteNoise |
| **Web Server** | Gunicorn |
| **Frontend** | Bootstrap 5, Custom CSS |
| **Deployment** | Render |

## 🔐 Role-Based Access Control

| Role | Capabilities |
|------|-------------|
| **Admin** (staff/superuser) | Full CRUD on all albums and photos; Django admin access |
| **Standard User** | Create own albums; upload photos to own albums; edit/delete only own content; view all albums |

## 📁 Project Structure

```
IPTAssignment6/
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── render.yaml                # Render deployment blueprint
├── build.sh                   # Render build script
├── Procfile                   # Gunicorn process file
├── photoalbum/                # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── albums/                    # Main application
│   ├── models.py              # Album & Photo models
│   ├── views.py               # All Class-Based Views
│   ├── forms.py               # ModelForms
│   ├── urls.py                # URL routing
│   ├── admin.py               # Django admin config
│   ├── mixins.py              # RBAC permission mixins
│   └── templatetags/          # Custom template filters
├── templates/                 # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── registration/          # Auth templates
│   └── albums/                # Album & Photo templates
└── static/
    ├── css/style.css          # Custom stylesheet
    └── js/main.js             # Client-side enhancements
```

## 🚀 Local Development Setup

### Prerequisites
- Python 3.10+
- pip
- A Cloudinary account ([sign up free](https://cloudinary.com/))

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd IPTAssignment6
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and fill in:
   - `SECRET_KEY` — Generate one with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - `CLOUDINARY_URL` — From your Cloudinary dashboard (format: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`)
   - `DEBUG=True` for local development

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (Admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Visit:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

## ☁️ Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `your-random-secret-key` |
| `DEBUG` | Debug mode (True/False) | `False` |
| `DATABASE_URL` | Database connection string | `postgresql://user:pass@host/db` |
| `CLOUDINARY_URL` | Cloudinary credentials | `cloudinary://key:secret@cloud` |
| `ALLOWED_HOSTS` | Comma-separated hostnames | `.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | Trusted origins for CSRF | `https://*.onrender.com` |

## 🌐 Deployment to Render

### Option 1: One-Click with Blueprint
1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click **New** → **Blueprint**
4. Connect your repo — `render.yaml` auto-configures everything
5. Set the `CLOUDINARY_URL` environment variable manually in the Render dashboard

### Option 2: Manual Setup
1. Create a **PostgreSQL** database on Render
2. Create a **Web Service** with:
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn photoalbum.wsgi:application`
3. Add all environment variables from the table above
4. Deploy!

### Post-Deployment
- Create an admin user: Go to your Render service **Shell** tab and run:
  ```bash
  python manage.py createsuperuser
  ```

## 📋 API / URL Endpoints

| URL | View | Method | Access |
|-----|------|--------|--------|
| `/` | Home | GET | Public |
| `/signup/` | Sign Up | GET/POST | Public |
| `/accounts/login/` | Login | GET/POST | Public |
| `/accounts/logout/` | Logout | POST | Auth |
| `/albums/` | Album List | GET | Auth |
| `/albums/create/` | Create Album | GET/POST | Auth |
| `/albums/<pk>/` | Album Detail | GET | Auth |
| `/albums/<pk>/edit/` | Edit Album | GET/POST | Owner/Admin |
| `/albums/<pk>/delete/` | Delete Album | GET/POST | Owner/Admin |
| `/albums/<pk>/photos/add/` | Upload Photo | GET/POST | Owner/Admin |
| `/albums/photos/<pk>/` | Photo Detail | GET | Auth |
| `/albums/photos/<pk>/delete/` | Delete Photo | GET/POST | Owner/Admin |
| `/admin/` | Django Admin | GET | Staff |

## 📄 License

This project was developed as an academic assignment for IPT (Integrative Programming and Technologies).
