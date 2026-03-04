# 📝 Task Management REST API

Ever wanted to keep track of your tasks without forgetting them? 
That's exactly what this project does — a simple but powerful 
REST API to manage your tasks, built with Python and FastAPI! 🚀

## 🤔 What does it do?
You can Create, Read, Update and Delete tasks — what developers 
call CRUD operations. All data is stored safely in MongoDB Atlas 
(a cloud database), so nothing gets lost!

## 🛠️ Tech Stack
- 🐍 Python
- ⚡ FastAPI
- ☁️ MongoDB Atlas
- ✅ Pydantic (for data validation)
- 🦄 Uvicorn (server)

## 📌 API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | / | Is the API alive? Check here! |
| POST | /tasks | Got a new task? Add it! |
| GET | /tasks | Show me all my tasks! |
| PUT | /tasks/{id} | Oops, need to update a task? |
| DELETE | /tasks/{id} | Done with a task? Delete it! |

## 🔒 Security
Database credentials are stored in a `.env` file — 
because hardcoding passwords is a crime! 😄

## 🧪 Testing
All endpoints were tested using Swagger UI — 
FastAPI's built in interactive API testing tool!

## 💡 What I learned
- How REST APIs work in real life
- Connecting Python to a cloud database
- Keeping secrets safe with environment variables
- Data validation using Pydantic
  
## 📚 Project Report
This project was developed as a self-practice project to learn REST API development using Python and FastAPI (2025).
