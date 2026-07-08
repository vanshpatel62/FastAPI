# FastAPI CRUD API with PostgreSQL

## Introduction

This project is a RESTful API built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Pydantic**. It follows a clean layered architecture that separates routing, business logic, database models, and data validation. The project is designed to be scalable, maintainable, and easy to understand, making it suitable for learning FastAPI best practices as well as building production-ready APIs.

---

# Tech Stack

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| Python 3.x   | Programming Language            |
| FastAPI      | Web Framework                   |
| PostgreSQL   | Relational Database             |
| SQLAlchemy   | ORM (Object Relational Mapper)  |
| Pydantic     | Data Validation & Serialization |
| Uvicorn      | ASGI Server                     |
| Logging      | Application Logging             |
| Git & GitHub | Version Control                 |

---

# What This Project Does

This project provides REST APIs for managing an e-commerce system.

### Features

* Customer Management
* Product Management
* Order Management
* Order Item Management
* Payment Management
* CRUD Operations
* Request & Response Validation
* Database Integration using SQLAlchemy
* Centralized Logging
* Exception Handling
* Automatic API Documentation using Swagger UI

---

# Project Structure

```text
app/
├── __init__.py
├── database.py
├── main.py
├── middleware.py
├── __init__.py
│
├── Models/
│   ├── customer.py
│   ├── order.py
│   ├── order_item.py
│   ├── payment.py
│   ├── product.py
│   └── __init__.py
│
├── Routers/
│   ├── customer.py
│   ├── order.py
│   ├── order_item.py
│   ├── payment.py
│   └── products.py
│
├── Schemas/
│   ├── customer.py
│   ├── order.py
│   ├── order_item.py
│   ├── payment.py
│   ├── product.py
│   └── __init__.py
│
└── Services/
    ├── customer.py
    ├── order.py
    ├── order_item.py
    ├── payment.py
    ├── product.py
    └── __init__.py
```

### Folder Description

| Folder/File     | Description                                                                           |
| --------------- | ------------------------------------------------------------------------------------- |
| `main.py`       | Entry point of the FastAPI application. Registers routers and starts the application. |
| `database.py`   | Creates the SQLAlchemy engine, session, and database dependency.                      |
| `middleware.py` | Contains custom middleware for request processing and logging.                        |
| `Models/`       | SQLAlchemy ORM models representing database tables.                                   |
| `Schemas/`      | Pydantic models for request validation and API responses.                             |
| `Routers/`      | Defines API endpoints for each module.                                                |
| `Services/`     | Contains business logic and database operations.                                      |

---

# Requirements

* Python 3.10 or later
* PostgreSQL
* Git
* pip

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# Installation & Run Project

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=postgres
DB_PASSWORD=your_password
```

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

| Documentation | URL                           |
| ------------- | ----------------------------- |
| Swagger UI    | `http://127.0.0.1:8000/docs`  |
| ReDoc         | `http://127.0.0.1:8000/redoc` |

These interfaces allow you to:

* View all available endpoints.
* Send API requests directly from the browser.
* Inspect request and response models.
* Test APIs without using external tools.

---

# Architecture

The project follows a layered architecture to separate responsibilities and improve maintainability.

```text
                Client
                   │
                   ▼
            FastAPI Application
                   │
                   ▼
              Middleware
                   │
                   ▼
               API Router
                   │
                   ▼
             Service Layer
                   │
                   ▼
         SQLAlchemy Session
                   │
                   ▼
              PostgreSQL
```

### Request Flow

1. The client sends an HTTP request.
2. Middleware processes the incoming request.
3. The appropriate router receives the request.
4. The router calls the corresponding service.
5. The service performs business logic and interacts with the database.
6. SQLAlchemy executes queries on PostgreSQL.
7. The response is returned through the service and router back to the client.
