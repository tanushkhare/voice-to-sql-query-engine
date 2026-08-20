import re
from typing import Dict, Any, List

class VoiceSQLCompiler:
    def __init__(self):
        # Database schema metadata definition
        self.schema_metadata = {
            "employees": ["id", "name", "department", "salary", "hire_date", "performance_score"],
            "orders": ["order_id", "customer_id", "total_amount", "order_date", "status"],
            "products": ["product_id", "name", "category", "price", "stock_quantity"]
        }

    def _sanitize_and_validate(self, sql: str) -> bool:
        # Prevent destructive operations (DML/DDL injection guardrail)
        forbidden = ["drop", "delete", "truncate", "alter", "update", "insert", ";--"]
        sql_lower = sql.lower()
        return not any(re.search(r"\b" + re.escape(word) + r"\b", sql_lower) for word in forbidden)

    def compile_natural_query(self, query_text: str, table: str = "employees") -> Dict[str, Any]:
        q = query_text.lower()
        cols = self.schema_metadata.get(table, self.schema_metadata["employees"])
        
        # Rule-based semantic parser compiling query intent to SQL
        if "highest" in q or "top" in q or "max" in q:
            if "salary" in q:
                sql = f"SELECT name, department, salary FROM {table} ORDER BY salary DESC LIMIT 5;"
                explanation = "Identified ordering intent on 'salary' with descending limit."
            elif "price" in q:
                sql = f"SELECT name, category, price FROM products ORDER BY price DESC LIMIT 5;"
                explanation = "Identified ordering intent on 'price' with descending limit."
            else:
                sql = f"SELECT * FROM {table} ORDER BY id DESC LIMIT 5;"
                explanation = "Standard descending query on primary key."
        elif "average" in q or "avg" in q:
            if "salary" in q and "department" in q:
                sql = f"SELECT department, AVG(salary) AS avg_salary FROM {table} GROUP BY department;"
                explanation = "Aggregated average salary grouped by department."
            else:
                sql = f"SELECT AVG(salary) AS average_salary FROM {table};"
                explanation = "Aggregate calculation of mean salary metric."
        elif "count" in q or "how many" in q or "number of" in q:
            sql = f"SELECT department, COUNT(*) AS total_count FROM {table} GROUP BY department;"
            explanation = "Calculated record counts categorized by department."
        elif "department" in q:
            match = re.search(r"in (engineering|sales|marketing|finance|hr)", q)
            dept = match.group(1).title() if match else "Engineering"
            sql = f"SELECT * FROM {table} WHERE department = '{dept}';"
            explanation = f"Filtered rows where department matches '{dept}'."
        else:
            sql = f"SELECT * FROM {table} LIMIT 10;"
            explanation = f"General retrieval limited to 10 rows from '{table}'."

        is_safe = self._sanitize_and_validate(sql)

        # Mock result rows for pipeline preview
        simulated_data = [
            {"id": 101, "name": "Sarah Chen", "department": "Engineering", "salary": 145000, "performance_score": 4.9},
            {"id": 102, "name": "Marcus Vance", "department": "Engineering", "salary": 138000, "performance_score": 4.7},
            {"id": 103, "name": "Elena Rostova", "department": "Sales", "salary": 125000, "performance_score": 4.6}
        ]

        return {
            "natural_query": query_text,
            "generated_sql": sql,
            "is_safe": is_safe,
            "explanation": explanation,
            "simulated_result": simulated_data
        }

sql_compiler = VoiceSQLCompiler()
