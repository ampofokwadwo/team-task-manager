from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from typing import Optional

app = FastAPI(title="Team Task Manager", description="A simple task management system for teams")

# User model
class User(BaseModel):
    model_config = ConfigDict(frozen=False)
    user_id: int
    name: str
    email: str

# Task model
class Task(BaseModel):
    model_config = ConfigDict(frozen=False)
    task_id: int
    title: str
    description: str
    status: str
    assignee_id: int

# Task Manager
class TaskManager:
    def __init__(self):
        self.users = []
        self.tasks = []

    def create_user(self, name: str, email: str):
        user = User(user_id=len(self.users) + 1, name=name, email=email)
        self.users.append(user)
        return user

    def create_task(self, title: str, description: str, assignee_id: int):
        task = Task(task_id=len(self.tasks) + 1, title=title, description=description, status="pending", assignee_id=assignee_id)
        self.tasks.append(task)
        return task

    def assign_task(self, task_id: int, assignee_id: int):
        for task in self.tasks:
            if task.task_id == task_id:
                task.assignee_id = assignee_id
                return task
        raise HTTPException(status_code=404, detail="Task not found")

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None, status: Optional[str] = None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if status:
                    task.status = status
                return task
        raise HTTPException(status_code=404, detail="Task not found")

    def delete_task(self, task_id: int):
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                del self.tasks[i] 
                return {"message": "Task deleted successfully"}
        raise HTTPException(status_code=404, detail="Task not found")

    def delete_user(self, user_id: int):
        for i, user in enumerate(self.users):
            if user.user_id == user_id:
                del self.users[i]
                return {"message": "User deleted successfully"}
        raise HTTPException(status_code=404, detail="User not found")

    def filter_tasks(self, status: Optional[str] = None, assignee_id: Optional[int] = None):
        filtered_tasks = []
        for task in self.tasks:
            if (status is None or task.status == status) and (assignee_id is None or task.assignee_id == assignee_id):
                filtered_tasks.append(task)
        return filtered_tasks

task_manager = TaskManager()

# Creating new user
@app.post("/users/")
async def create_user(name: str, email: str):
    user = task_manager.create_user(name, email)
    return user

# Creating new task
@app.post("/tasks/")
async def create_task(title: str, description: str, assignee_id: int):
    task = task_manager.create_task(title, description, assignee_id)
    return task

# Assigning task to user
@app.put("/tasks/{task_id}/assign/")
async def assign_task(task_id: int, assignee_id: int):
    task_manager.assign_task(task_id, assignee_id)
    return {"message": "Task assigned successfully"}

# Updating task status
@app.put("/tasks/{task_id}/update/")
async def update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None, status: Optional[str] = None):
    task_manager.update_task(task_id, title, description, status)
    return {"message": "Task updated successfully"}

# Deleting user
@app.delete("/users/{user_id}/")
async def delete_user(user_id: int):
    user = next((user for user in task_manager.users if user.user_id == user_id), None)
    if user:
        task_manager.users.remove(user)
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Deleting task
@app.delete("/tasks/{task_id}/")
async def delete_task(task_id: int):
    result = task_manager.delete_task(task_id)
    return result

# Filtering tasks by status
@app.get("/tasks/")
async def filter_tasks(status: Optional[str] = None, assignee_id: Optional[int] = None):
    tasks = task_manager.filter_tasks(status, assignee_id)
    return tasks

