from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import collection
from bson import ObjectId

app = FastAPI()

def serialize_task(task):
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "completed": task["completed"]
    }
class Task(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5)
    completed: bool = False

# Home route
@app.get("/")
def home():
    return {"message": "API is working"}

# Create task
@app.post("/tasks")
def create_task(task: Task):
    try:
        result = collection.insert_one(task.dict())
        return {"message": "Task added", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get all tasks
@app.get("/tasks")
async def get_tasks():
    tasks = collection.find()
    return [serialize_task(task) for task in tasks]

# Update task
@app.put("/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task):
    try:
        result = collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": updated_task.dict()}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task updated"}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Task ID")

# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted"}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Task ID")
