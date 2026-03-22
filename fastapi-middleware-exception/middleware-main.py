# Middleware and Exception Handling in FastAPI
# You are building a FastAPI application that logs every incoming request.

# First, create a simple API endpoint /hello that returns the following JSON response:

# {
#   "message": "Hello, Welcome to FastAPI!"
# }
# Next, create a middleware that:

# Logs the HTTP method (GET, POST, etc.)
# Logs the URL path of the request
# Prints a message before the request is processed
# Prints a message after the response is returned
# Finally, implement a simple exception handler for 404 Not Found errors. This handler should return a custom JSON message when a user tries to access a route that is not defined in the application (for example, /unknown).

# Example response for an undefined route:

# {
#   "message": "The requested resource was not found"
# }

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time
import asyncio

app = FastAPI()
# Middleware to log incoming requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Response: {response.status_code} in {process_time:.2f}s")
    return response

# API endpoint /hello
@app.get("/hello")
async def hello():
    return {"message": "Hello, Welcome to FastAPI!"}
# Exception handler for 404 Not Found errors
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "The requested resource was not found"},
    )