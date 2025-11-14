
---

# 🧾 **README.md for Todo List API (Built with FastAPI)**

```markdown
# ✅ Todo List API (Built with FastAPI)

A simple and educational **Todo List REST API** built with **FastAPI**, demonstrating clean API design, CRUD operations, and in-memory data storage (no external database yet).  
This project is structured following **FastAPI best practices** — using Pydantic models, route separation, and data validation.

---

## 🚀 Features

- User Registration and Retrieval
- Task Creation, Retrieval, and Update
- In-Memory Database Simulation (Python dictionary)
- Pydantic Models for Request/Response Validation
- Proper HTTP Status Codes and Error Handling
- Clear API Endpoints for Easy Testing with Postman or cURL

---

## 🧱 Tech Stack

- **Backend Framework:** FastAPI  
- **Language:** Python 3.10+  
- **Validation:** Pydantic  
- **Runtime Server:** Uvicorn  
- **Containerization:** Docker  

---

## 📂 Project Structure

```

todo_app/
│
├── main.py                # Entry point of the application
├── models.py              # Pydantic models for Users & Tasks
├── database.py            # In-memory database simulation
├── routes/
│   ├── users.py           # All user-related endpoints
│   └── tasks.py           # All task-related endpoints
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image definition
└── README.md              # Project documentation

````

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/todo-list-fastapi.git
cd todo-list-fastapi
````

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

Now visit 👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** to open the Swagger UI for API testing.

---

## 🧪 Example Endpoints

### 🧍 User Endpoints

| Method | Endpoint | Description         |
| ------ | -------- | ------------------- |
| `POST` | `/users` | Register a new user |
| `GET`  | `/users` | Get all users       |

### 📝 Task Endpoints

| Method  | Endpoint              | Description                   |
| ------- | --------------------- | ----------------------------- |
| `POST`  | `/tasks?user_id={id}` | Create a new task for a user  |
| `GET`   | `/tasks?id={id}`      | Get tasks for a specific user |
| `GET`   | `/tasks/all`          | Get all tasks in the database |
| `PATCH` | `/tasks`              | Update task details           |

---

## 🐳 Running with Docker

### 1. Build the Docker Image

```bash
docker build -t fastapi-todo-app .
```

### 2. Run the Container

```bash
docker run -d -p 8000:8000 fastapi-todo-app
```

### 3. Access the API

Visit:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)
to use the interactive Swagger UI.

---

## 🧰 Example Request Bodies

### Create a User

```json
{
  "username": "iceking",
  "password": "1234"
}
```

### Create a Task

```json
{
  "title": "Learn FastAPI",
  "description": "Build a simple Todo app"
}
```

---

## 📘 API Documentation

FastAPI automatically generates documentation:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧑‍💻 Author

**👤 iiceekiing**
Fullstack Software Engineer | Web3 Developer
🔗 [LinkedIn](https://linkedin.com/in/iiceekiing)
🔗 [X (Twitter)](https://x.com/iiceekiing)

---

## 🪶 License

This project is open-source and available under the **MIT License**.

````

---