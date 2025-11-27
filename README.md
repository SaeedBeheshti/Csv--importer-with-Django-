# Csv--importer-with-Django-


This project is a Django + Django REST Framework (DRF) application for importing CSV files asynchronously. It uses JWT authentication for API security, Swagger for API documentation, Celery with Redis for background processing, and PostgreSQL as the database. The project is containerized using Docker.

## Features

- JWT-based authentication for API endpoints
- Swagger API documentation
- CSV import with asynchronous processing (Celery + Redis)
- Error logging for CSV imports (JSONField)
- PostgreSQL database
- Dockerized setup

## Tech Stack

- Python 3.11+
- Django 5.x
- Django REST Framework
- Celery
- Redis
- PostgreSQL
- Docker & Docker Compose
- Swagger (drf-yasg or drf-spectacular)

## Project Structure
