from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import query

app = FastAPI(
    title="Voice-to-SQL Query Engine API",
    version="1.0.0",
    description="Microservice translating natural voice transcripts into structured SQL commands."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router)

@app.get("/")
def read_root():
    return {"message": "Voice-to-SQL Backend Engine is online!"}