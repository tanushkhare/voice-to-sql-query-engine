from fastapi import APIRouter, HTTPException
from backend.app.schemas.sql_schema import NaturalQueryRequest, SQLGenerationResponse
from backend.app.services.sql_compiler_service import sql_compiler

router = APIRouter(prefix="/api/v1/sql", tags=["Voice to SQL Compiler"])

@router.post("/generate", response_model=SQLGenerationResponse)
async def generate_sql(payload: NaturalQueryRequest):
    try:
        result = sql_compiler.compile_query(payload.query_text, payload.target_table)
        return SQLGenerationResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
