from fastapi import FastAPI
from api.todo_items import router as todo_router
from api.users import router as user_router
from models import todo
from depenedencies.database import engine




todo.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router, prefix="/todo")
app.include_router(user_router, prefix="/users")




@app.get("/")
async def health_check():
    print()
    return {"OK": True}



