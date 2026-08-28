from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class NaturalQueryRequest(BaseModel):
    query_text: str = Field(..., min_length=3, description="Natural language query or intent")
    target_table: Optional[str] = Field(default="employees", description="Target database table")

class SQLGenerationResponse(BaseModel):
    natural_query: str
    target_table: str
    generated_sql: str
    is_safe: bool
    explanation: str
    simulated_result: List[Dict[str, Any]]
