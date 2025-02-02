# FAQ Management System

## Overview
The FAQ Management System is a Django-based REST API that allows users to manage frequently asked questions with multi-language support and rich-text formatting.

## Features
- ✅ **CRUD operations** for FAQs
- ✅ **Multi-language support** (English, Hindi, Bengali, French, Spanish)
- ✅ **Rich-text formatting** with CKEditor
- ✅ **REST API with Django Rest Framework (DRF)**
- ✅ **Asynchronous translation with Celery & Redis**
- ✅ **Caching using Django cache framework**
- ✅ **Unit Tests & Code Quality**
  - ✔️ API response validation
  - ✔️ Model methods testing
  - ✔️ PEP8 compliance with flake8 linting

## Directory Structure
```
faq_project/
│── config/                # Main project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   ├── celery.py          # Celery configuration
│── faq_project/           # Main app folder
│   ├── migrations/        # Database migrations
│   ├── models.py          # FAQ model definition
│   ├── views.py           # API views
│   ├── serializers.py     # DRF serializers
│   ├── tasks.py           # Celery tasks for translations
│   ├── urls.py            # App-specific URL routing
│   ├── tests.py           # Unit tests
│── db.sqlite3             # SQLite database (change for production)
│── manage.py              # Django management script
│── venv/                  # Python virtual environment
```

## Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone <repo_url>
cd faq_project
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Run Development Server**
```bash
python manage.py runserver
```

### **6️⃣ Start Celery & Redis**
Make sure Redis is running before starting Celery.
```bash
celery -A config worker --loglevel=info
```

## API Endpoints
### **Base URL:** `http://127.0.0.1:8000/`

| Method | Endpoint       | Description |
|--------|---------------|-------------|
| GET    | `/`           | API Home    |
| GET    | `/faqs/`      | List FAQs   |
| POST   | `/faqs/`      | Create FAQ  |

## Running Tests
```bash
python manage.py test faq_project
```

## Code Quality & Linting
```bash
flake8 .
```

## License
This project is licensed under the MIT License.

