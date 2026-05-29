from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []
task_id_counter = 1


# ---------- MODEL ----------
class Task(BaseModel):
    name: str


# ---------- ROUTES ----------
@app.get("/")
def home():
    return {"message": "Task Manager API is running"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "name": task.name,
        "done": False
    }

    tasks.append(new_task)
    task_id_counter += 1

    return new_task


@app.put("/tasks/{task_id}")
def mark_done(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")