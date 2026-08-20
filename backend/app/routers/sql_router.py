from fastapi import APIRouter, HTTPException, UploadFile, File
from backend.app.schemas.sql_schema import NaturalQueryRequest, SQLGenerationResponse
from backend.app.services.sql_compiler_service import sql_compiler

router = APIRouter(prefix="/api/v1/sql", tags=["Voice & Natural Language to SQL Engine"])

@router.post("/generate", response_model=SQLGenerationResponse)
async def generate_sql_from_text(payload: NaturalQueryRequest):
    try:
        result = sql_compiler.compile_natural_query(payload.query_text, payload.target_table)
        return SQLGenerationResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/transcribe-and-generate", response_model=SQLGenerationResponse)
async def transcribe_audio_to_sql(audio_file: UploadFile = File(...)):
    # Simulated voice-to-text transcription boundary for audio inputs
    transcribed_text = "Show me all employees in engineering with the highest salary"
    result = sql_compiler.compile_natural_query(transcribed_text, "employees")
    return SQLGenerationResponse(**result)
