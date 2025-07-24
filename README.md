# 📝 Task Management API

## 🧩 Overview

This is a full-featured **RESTful API** designed for managing users, groups, and tasks. The system allows you to register users, authenticate via JWT, assign users to groups, and manage tasks within those groups. It is built with **FastAPI** for high performance and ease of use, and **MongoDB** for flexible, document-based storage. The codebase is modular and adheres to a layered architecture to ensure clean separation of concerns and scalability.

---

## 🔧 Purpose & Use Case

This API is ideal for task management scenarios such as:

- Team productivity tools
- Group collaboration platforms
- Educational group project coordinators
- Lightweight internal task trackers

It supports multiple user accounts, group assignments, and fine-grained control over task distribution and access.

---

## 🚀 Core Features

### 🔐 Authentication

- Secure JWT-based login system
- Passwords are stored in hashed format using bcrypt
- `.env` configuration allows changing secrets without hardcoding

### 👤 User Management

- Register new users via `/auth/register`
- Login and receive an access token via `/auth/login`
- List all registered users via `/users/`

### 👥 Group Management

- Create new groups via `/groups/`
- Assign users to specific groups
- Organize tasks within these groups

### ✅ Task Management

- Add tasks via `/tasks/`, each linked to a group and its members
- Retrieve tasks per group with `/tasks/group/{group_id}`
- Tasks can be filtered, retrieved, and extended to include metadata like deadlines, status, or assignees

### 📂 Architecture Highlights

- **Routing Layer**: Defines API endpoints, validates inputs, and delegates logic to services
- **Service Layer**: Handles business logic like validations, authorization, user-role checks
- **Repository Layer**: Handles direct database interaction (CRUD operations on MongoDB)
- **Model Layer**: Represents core domain models (User, Task, Group)
- **Schema Layer**: Provides serialization & transformation logic for responses

---

## 🏗️ Technology Stack

- **FastAPI** – modern Python framework for building APIs quickly
- **MongoDB** – flexible NoSQL document storage
- **Pydantic** – input validation and data parsing
- **PyJWT** – JWT encoding/decoding
- **bcrypt** – password hashing
- **Uvicorn** – lightning-fast ASGI server for running FastAPI

---

## 📁 Project Structure

```
PythonProject/
├── app/
│   ├── main.py                  # Entry point
│   ├── db/dbconn.py            # MongoDB connection setup
│   ├── auth/                   # Auth functions and JWT token handler
│   ├── model/                  # Data models: User, Group, Task
│   ├── repository/             # DB interaction logic
│   ├── routes/                 # API endpoint definitions
│   ├── schema/serializer.py    # Serialization helpers
│   └── service/                # Business logic handlers
└── requirements.txt            # Dependencies
```

---

## ▶️ Running the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/ablondu21/PyProjectAPI
cd PyProjectAPI
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file in `app/` with:

```env
MONGO_URL=mongodb://localhost:27017/
JWT_SECRET=super_secret_key
```

### 4. Start the development server

```bash
uvicorn app.main:app --reload
```

Go to [http://localhost:8000/docs](http://localhost:8000/docs) to explore the auto-generated Swagger UI.

---

## 🔍 API Overview

| Endpoint                  | Method | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| `/auth/register`          | POST   | Register a new user                |
| `/auth/login`             | POST   | Login and receive JWT              |
| `/users/`                 | GET    | Get all registered users           |
| `/groups/`                | POST   | Create a new group                 |
| `/tasks/`                 | POST   | Create a new task for a group      |
| `/tasks/group/{group_id}` | GET    | List tasks associated with a group |

> All endpoints (except register/login) require a valid JWT token via `Authorization: Bearer <token>` header.

---

## 🛡️ Security Considerations

- JWT tokens expire and can be rotated as needed
- Passwords are hashed with bcrypt before being stored
- MongoDB access is abstracted via a single connection handler
- Environment configuration (e.g., DB URI, JWT secret) is externalized

---

## 📌 Future Improvements

- [ ] Role-based access control (admin/user distinction)
- [ ] Advanced task filtering (due date, status, tags)
- [ ] Unit & integration tests (via pytest)
- [ ] Dockerfile & docker-compose for containerized deployment
- [ ] CI/CD pipeline for GitHub Actions

---

## 👨‍💻 Author

Developed with ❤️ by Matei Alexandru
