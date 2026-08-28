from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import sql_router
import uvicorn

app = FastAPI(
    title="Voice-to-SQL Query Engine API",
    description="AST-sandboxed natural language to SQL transpilation service.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sql_router.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "voice-to-sql-query-engine"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
