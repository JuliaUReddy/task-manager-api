# Task Manager API (FastAPI)

A simple REST API built using Python and FastAPI.

## Features
- Create tasks
- View tasks
- Mark tasks as complete
- Delete tasks
- RESTful API architecture

## Tech Stack
- Python
- FastAPI
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /tasks | Retrieve all tasks |
| POST | /tasks | Create a task |
| PUT | /tasks/{id} | Mark task as complete |
| DELETE | /tasks/{id} | Delete a task |

## Run Locally

```bash
uvicorn main:app --reload
```