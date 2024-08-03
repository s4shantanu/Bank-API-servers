# Bank-API-servers

This project implements an API server using Django, Django REST Framework, and Graphene-Django to manage bank branch data. The API supports both REST and GraphQL endpoints for querying bank and branch details.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/bank-data-api.git
    cd bank-data-api
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install django djangorestframework graphene-django
    ```

4. **Create a new Django project and app:**
    ```bash
    django-admin startproject bank_data
    cd bank_data
    django-admin startapp branches
    ```

## Configuration

### 1. Defining Models

Define `Bank` and `Branch` models in `branches/models.py`:

```python
# branches/models.py

from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length