from fastapi import APIRouter
from app.schemas.query import VoiceQueryRequest, SQLQueryResponse
from app.services.nlp_service import process_voice_to_sql

router = APIRouter(prefix="/api", tags=["Voice-to-SQL Engine"])

@router.post("/convert", response_model=SQLQueryResponse)
def convert_query(payload: VoiceQueryRequest):
    return process_voice_to_sql(payload.transcript)