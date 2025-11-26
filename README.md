# ALX Travel App - Backend (Django)

This project is a backend application for a travel booking platform built using **Django** and **Django REST Framework (DRF)**. It demonstrates how to:

- Model relational data in Django
- Serialize data for API endpoints
- Seed a database with sample data
- Use Docker for development and deployment

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup & Installation](#setup--installation)
- [Using Docker](#using-docker)
- [Database Seeding](#database-seeding)
- [Testing the API](#testing-the-api)
- [Learning Outcomes](#learning-outcomes)

---

## Project Overview

The ALX Travel App backend handles the following:

- **Listings**: Properties available for booking
- **Bookings**: Records of user reservations
- **Reviews**: User feedback on listings

The project uses **PostgreSQL** as the database and provides a **REST API** to interact with the models.

---

## Features

- Django ORM models with relationships and constraints
- Django REST Framework serializers for API data
- Management command to seed database (`python manage.py seed`)
- Dockerized development environment
- Fully reproducible setup for testing and development

---

## Project Structure

```

alx_travel_app_0x00/
│
├─ alx_travel_app/         # Django project folder
│  ├─ settings.py          # Project settings
│  ├─ urls.py              # URL routing
│
├─ listings/               # Django app for core models
│  ├─ models.py            # Listing, Booking, Review models
│  ├─ serializers.py       # DRF serializers
│  ├─ management/
│  │  └─ commands/
│  │     ├─ **init**.py
│  │     └─ seed.py        # Seeder script
│  └─ views.py
│
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
└─ README.md

````

---

## Requirements

- Docker & Docker Compose
- Python 3.11 (inside container)
- Django 4.x
- Django REST Framework
- PostgreSQL 15.x (Docker container)

---

## Setup & Installation (Docker)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/alx_travel_app_0x00.git
cd alx_travel_app_0x00
````

### 2. Create `requirements.txt` inside `alx_travel_app/`

Example:

```
Django>=4.2
djangorestframework
psycopg2-binary
django-seed
```

### 3. Build and run Docker containers

```bash
docker compose up --build -d
```

* `-d` runs containers in detached mode
* The **web** container runs Django commands
* The **db** container runs PostgreSQL

### 4. Enter the Django container (optional)

```bash
docker compose exec web bash
```

---

## Database Setup

### 1. Make migrations

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

### 2. Seed the database

```bash
docker compose exec web python manage.py seed
```

> This will populate your database with sample listings for testing.

---

## Testing the API

After starting the containers, you can run the development server:

```bash
docker compose exec web python manage.py runserver 0.0.0.0:8000
```

* Access API endpoints: `http://localhost:8000/api/listings/`
* Use **Postman** or **curl** to test endpoints

---

## Learning Outcomes

By completing this project, you will learn how to:

1. Define Django models with relationships and constraints
2. Serialize model data using Django REST Framework
3. Automate database seeding with custom management commands
4. Run a full Django/PostgreSQL stack using Docker
5. Prepare a backend API for real-world travel booking applications

---

## Notes

* Make sure `listings` is added to `INSTALLED_APPS` in `settings.py`.
* Ensure all `__init__.py` files exist in `management` and `commands` folders.
* Rebuild Docker containers whenever you update dependencies:

```bash
docker compose down
docker compose up --build -d
```

---

Happy coding! ✨

