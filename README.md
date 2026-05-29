# Task Manager API (FastAPI)

A simple REST API built with Python and FastAPI.

## Features
- Create tasks
- View tasks
- Mark tasks as complete
- Delete tasks
- REST API structure
- Basic input validation

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Pydantic

## API Endpoints
- GET /tasks
- POST /tasks
- PUT /tasks/{id}
- DELETE /tasks/{id}

## Run Project
```bash
uvicorn main:app --reload
```