from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
async def search(name: str = None, age: int = None):
    """
    GET endpoint that accepts optional query parameters name and age
    Returns the received parameters as JSON
    """
    return {"name": name, "age": age}