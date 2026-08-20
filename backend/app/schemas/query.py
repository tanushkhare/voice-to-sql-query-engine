from pydantic import BaseModel

class VoiceQueryRequest(BaseModel):
    transcript: str

class SQLQueryResponse(BaseModel):
    transcript: str
    generated_sql: str
    confidence_score: float
    execution_status: str