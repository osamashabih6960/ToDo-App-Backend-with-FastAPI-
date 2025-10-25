# ToDo FastAPI Project 🗂️

## Overview 🌟

This project is a simple ToDo application built with FastAPI and SQLAlchemy. It allows users to create, read, update, and delete ToDo items using a RESTful API. The database used for this project is SQLite.

## Project Structure 📂

```
todo_api_project/
│
├── api/
│   ├── database/
│   │   ├── db_engine.py          # 🔧 Database engine configuration and session management
│   │   ├── schemas.py            # 🗂️ SQLAlchemy ORM models for the database schema
│   │
│   ├── routes/
│   │   └── models.py             # 📝 Pydantic models for request and response validation
│
├── main.py                       # 🚀 FastAPI application with API routes
├── requirements.txt              # 📦 Project dependencies
└── README.md                     # 📖 This file
```

## Components 🛠️

1. **Database Configuration (`api/database/db_engine.py`)**:
   - Uses SQLAlchemy to connect to an SQLite database.
   - Provides a function `get_db` to manage database sessions.

2. **Models (`api/routes/models.py`)**:
   - `ToDoCreate`: Pydantic model for validating data when creating or updating a ToDo item.
   - `ToDoResponse`: Pydantic model for serializing the response of ToDo items.

3. **Schemas (`api/database/schemas.py`)**:
   - `ToDo`: SQLAlchemy model representing the ToDo table in the database.

4. **Main Application (`main.py`)**:
   - Defines FastAPI routes to handle CRUD operations on ToDo items.
   - Includes endpoints for creating, reading, updating, and deleting ToDo items.

## Endpoints 📡

### `GET /`

Fetches the first ToDo item from the database. Returns the item in `ToDoResponse` format.

**Response Example:**
```json
{
  "id": "some-uuid",
  "task_title": "Sample Task",
  "description": "This is a sample task",
  "created_at": "2025-10-04T12:00:00Z",
  "task_completed": false
}
```

### `PUT /{id}`

Updates a ToDo item identified by `id`. Requires `ToDoCreate` data for updates.

**Request Body Example:**
```json
{
  "task_title": "Updated Task",
  "description": "Updated description",
  "task_completed": true
}
```

**Response Example:**
```json
{
  "id": "some-uuid",
  "task_title": "Updated Task",
  "description": "Updated description",
  "created_at": "2025-10-04T12:00:00Z",
  "task_completed": true
}
```

### `POST /`

Creates a new ToDo item. Requires `ToDoCreate` data.

**Request Body Example:**
```json
{
  "task_title": "New Task",
  "description": "Description for new task",
  "task_completed": false
}
```

**Response Example:**
```json
{
  "id": "some-uuid",
  "task_title": "New Task",
  "description": "Description for new task",
  "created_at": "2025-10-04T12:00:00Z",
  "task_completed": false
}
```

### `DELETE /{id}`

Deletes the ToDo item identified by `id`.

**Response Example:**
```json
{
  "detail": "ToDo item deleted successfully"
}
```

## Setup ⚙️

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and Activate a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```sh
   uvicorn main:app --reload
   ```

5. **Database Migration:**
   - The database schema will be created automatically when you start the application, based on the models defined in `schemas.py`.

## Dependencies 📦

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (or any compatible SQLAlchemy database)

## Notes 📝

- Ensure that the `DATABASE_URL` in `db_engine.py` is correctly set to point to your SQLite database or adjust it for other database engines.
- The application uses SQLite in the local file `api/database/todo.db`. Ensure the directory exists or adjust the path as needed.
