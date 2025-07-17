from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

from router import story, job
# Explicitly import all model classes to ensure table registration
from models.story import Story
from models.job import StoryJob
from db.database import create_tables

create_tables()

app = FastAPI(
    title="Choose Your Own Adventure",
    description="A simple API to generate cool stories.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # Allows all origins, "*" allows any domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, "get", "post", etc.
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

app.include_router(story.router, prefix=settings.API_PREFIX)
app.include_router(job.router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)