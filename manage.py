# 💇‍♀️ PlatonicBeauty — Salon Booking Platform

A full-stack web platform for a men's and women's beauty salon, built with **Django 5** and **Django REST Framework**. The platform includes a public website, an online booking system, an admin dashboard, and a versioned REST API ready for iOS and Android mobile apps.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.1-green)
![DRF](https://img.shields.io/badge/DRF-3.15-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [API Documentation](#-api-documentation)
- [Screenshots](#-screenshots)
- [Deployment](#-deployment)
- [Roadmap](#-roadmap)
- [Author](#-author)
- [License](#-license)

---

## 🌟 Overview

**PlatonicBeauty** is a production-ready platform designed to handle the full workflow of a modern beauty salon — from letting customers browse services and book appointments online, to giving salon owners a powerful admin dashboard to manage stylists, services, bookings, and reviews.

The backend is built as a **modular, versioned REST API** so the same core can power:
-  The web frontend (Django templates + Tailwind CSS + HTMX)
- Native iOS and Android apps (via JSON API)
- Future third-party integrations

---

##  Features

### 👥 Customer-Facing
- Browse services by **gender** (men / women / unisex) and **category**
- View stylist profiles, specialties, and reviews
- Book appointments online — **no account required**
- Look up existing bookings using phone number + last 6 digits
- Read the beauty blog and browse the gallery

### 🛠 Admin Dashboard
- Manage services, categories, stylists, and working hours
- Confirm, reschedule, or cancel bookings
- Approve or reject customer reviews
- Upload gallery images and blog posts
- View reports on bookings and revenue

###  Security & Authentication
- **JWT authentication** (SimpleJWT) for mobile clients
- **CSRF protection** on all forms
- **Rate limiting** on public API endpoints
- Server-side validation for phone, email, date/time
- Environment-based secrets (`.env`) — no hardcoded keys

### Internationalization
- Multi-language support (English + Spanish)
- Timezone-aware booking system (`America/Los_Angeles`)
- RTL-ready for future Middle Eastern markets

###  Mobile-Ready API
- Versioned endpoints under `/api/v1/`
- Swagger + ReDoc documentation auto-generated
- Token refresh flow for long-lived mobile sessions
- Consistent JSON response format

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.12, Django 5.1, Django REST Framework |
| **Database** | PostgreSQL 16 (SQLite for local dev) |
| **Auth** | JWT (djangorestframework-simplejwt) |
| **API Docs** | drf-spectacular (Swagger + ReDoc) |
| **Frontend** | Django Templates, Tailwind CSS, HTMX, Alpine.js |
| **Task Queue** | Celery + Redis |
| **Static Files** | WhiteNoise |
| **Deployment** | Docker, Docker Compose, Nginx, Gunicorn |
| **Image Handling** | Pillow |
| **Env Management** | python-decouple |

---

##  Architecture

PlatonicBeauty follows a **modular app architecture** — each domain lives in its own Django app under `apps/`, which makes the codebase easy to extend, test, and maintain.

Manual deployment (Ubuntu VPS)
Install Python 3.12, PostgreSQL, Redis, Nginx.

Clone the repo and set up the virtual environment.

Configure .env with production values (DEBUG=False, real ALLOWED_HOSTS, database URL).

Run python manage.py collectstatic.

Start Gunicorn as a systemd service.

Configure Nginx as a reverse proxy.

Enable HTTPS with certbot (Let's Encrypt).

🗺 Roadmap
☑ Public website (services, stylists, gallery, blog)
☑ Online booking system
☑ Admin dashboard
☑ REST API v1 with JWT
☑ Multi-language support (EN / ES)
□ Online payment integration (Stripe)
□ SMS reminders (Twilio / Plivo)
□ iOS app
□ Android app
□ Push notifications
□ Analytics dashboard for salon owners
👨‍💻 Author
Fariborz Zamani
Full-Stack Django Developer — Tehran, Iran

 GitHub: @infozamani

📧 Email: fariborz400@gmail.com

I'm available for remote freelance and contract work. Feel free to reach out.

 License
This project is licensed under the MIT License. See the LICENSE file for details.

 Acknowledgements
Built with Django and Django REST Framework

UI powered by Tailwind CSS and HTMX

Icons by Heroicons
