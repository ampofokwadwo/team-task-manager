# 📋 Team Task Manager

A lightweight, in-memory REST API for managing team tasks and users, built with **FastAPI** and **Pydantic**.

---

## ✨ Features

- 👤 Create and delete team members
- ✅ Create, update, assign, and delete tasks
- 🔍 Filter tasks by status or assignee
- ⚡ Fast async endpoints powered by FastAPI
- 📖 Auto-generated interactive API docs (Swagger UI & ReDoc)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework |
| [Pydantic v2](https://docs.pydantic.dev/) | Data validation & models |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| [uv](https://github.com/astral-sh/uv) | Dependency management |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ampofokwadwo/team-task-manager.git
   cd team-task-manager
   ```

2. **Create and activate the virtual environment**
   ```bash
   uv venv
   # Windows (PowerShell)
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
   .venv\Scripts\Activate.ps1
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```

4. **Run the development server**
   ```bash
   uvicorn src.main:app --reload
   ```

5. **Open the API docs**
   - Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 API Reference

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/users/` | Create a new user |
| `DELETE` | `/users/{user_id}/` | Delete a user by ID |

#### Create User — `POST /users/`

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | `string` | ✅ | Full name of the user |
| `email` | `string` | ✅ | Email address of the user |

**Example Response:**
```json
{
  "user_id": 1,
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

---

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/tasks/` | Create a new task |
| `GET` | `/tasks/` | List / filter tasks |
| `PUT` | `/tasks/{task_id}/assign/` | Reassign a task to a user |
| `PUT` | `/tasks/{task_id}/update/` | Update task fields |
| `DELETE` | `/tasks/{task_id}/` | Delete a task |

#### Create Task — `POST /tasks/`

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | `string` | ✅ | Task title |
| `description` | `string` | ✅ | Task description |
| `assignee_id` | `integer` | ✅ | ID of the user to assign |

**Example Response:**
```json
{
  "task_id": 1,
  "title": "Design landing page",
  "description": "Create mockups for the new landing page",
  "status": "pending",
  "assignee_id": 1
}
```

#### Filter Tasks — `GET /tasks/`

**Query Parameters (all optional):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `status` | `string` | Filter by status (e.g. `pending`, `in_progress`, `done`) |
| `assignee_id` | `integer` | Filter by assigned user ID |

#### Update Task — `PUT /tasks/{task_id}/update/`

**Query Parameters (all optional):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | `string` | New task title |
| `description` | `string` | New task description |
| `status` | `string` | New task status |

---

## 📁 Project Structure

```
team-task-manager/
├── src/
│   └── main.py          # Application entry point — models, logic & routes
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock              # Locked dependency versions
└── README.md
```

---

## ⚠️ Notes

> [!NOTE]
> This API uses **in-memory storage**. All data is lost when the server restarts. For production use, integrate a database (e.g. PostgreSQL with SQLAlchemy or SQLModel).

> [!TIP]
> Task statuses are free-form strings. Consider standardizing to values like `pending`, `in_progress`, and `done` in your requests.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
