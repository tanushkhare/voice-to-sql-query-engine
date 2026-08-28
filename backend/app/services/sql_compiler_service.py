import re
from typing import Dict, Any, List

class VoiceSQLCompiler:
    ALLOWED_TABLES = {"employees", "orders", "products", "transactions", "customers"}
    FORBIDDEN_KEYWORDS = {"drop", "delete", "truncate", "alter", "insert", "update", "exec", "execute", ";", "--"}

    def compile_query(self, query_text: str, table: str = "employees") -> Dict[str, Any]:
        table_clean = table.strip().lower()
        if table_clean not in self.ALLOWED_TABLES:
            raise ValueError(f"Table access denied: '{table}'. Whitelist: {', '.join(sorted(self.ALLOWED_TABLES))}")

        query_lower = query_text.lower()
        
        # Check for injection or destructive patterns
        for keyword in self.FORBIDDEN_KEYWORDS:
            if re.search(r"\b" + re.escape(keyword) + r"\b", query_lower) or ";" in query_text or "--" in query_text:
                raise ValueError(f"Security validation rejected: Forbidden operation or punctuation detected: '{keyword}'")

        # Deterministic schema synthesis
        if "highest" in query_lower or "top" in query_lower or "max" in query_lower:
            sql = f"SELECT * FROM {table_clean} ORDER BY salary DESC LIMIT 5;"
            explanation = f"Aggregated top 5 records descending from {table_clean}."
        elif "count" in query_lower or "how many" in query_lower or "total" in query_lower:
            sql = f"SELECT COUNT(*) AS total_count FROM {table_clean};"
            explanation = f"Calculated total row count across {table_clean}."
        elif "average" in query_lower or "avg" in query_lower:
            sql = f"SELECT AVG(salary) AS average_metric FROM {table_clean};"
            explanation = f"Evaluated metric averages across {table_clean}."
        else:
            sql = f"SELECT * FROM {table_clean} LIMIT 10;"
            explanation = f"Retrieved standard record subset from {table_clean}."

        sample_rows = [
            {"id": 1, "name": "Alice Chen", "department": "Engineering", "salary": 145000, "status": "Active"},
            {"id": 2, "name": "Marcus Vance", "department": "Security", "salary": 138000, "status": "Active"},
            {"id": 3, "name": "Elena Rostova", "department": "Data", "salary": 152000, "status": "Active"}
        ]

        return {
            "natural_query": query_text,
            "target_table": table_clean,
            "generated_sql": sql,
            "is_safe": True,
            "explanation": explanation,
            "simulated_result": sample_rows
        }

sql_compiler = VoiceSQLCompiler()
