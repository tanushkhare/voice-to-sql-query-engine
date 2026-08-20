from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class NaturalQueryRequest(BaseModel):
    query_text: str = Field(..., min_length=5, description="Natural language query description")
    target_table: Optional[str] = Field(default="employees", description="Target database table context")

class SQLGenerationResponse(BaseModel):
    natural_query: str
    generated_sql: str
    is_safe: bool
    explanation: str
    simulated_result: List[Dict[str, Any]]
