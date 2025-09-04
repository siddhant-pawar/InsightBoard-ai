# app/main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import transcripts, tasks

# Create FastAPI app
app = FastAPI(title="InsightBoard AI API")

# Configure CORS
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Restrict in production using environment variable
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(transcripts.router)
app.include_router(tasks.router)

# Health check endpoint
@app.get("/healthz")
async def health():
    return {"status": "ok"}

# Optional: Logging requests for debugging
@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    print(f"{request.method} {request.url} -> {response.status_code}")
    return response
