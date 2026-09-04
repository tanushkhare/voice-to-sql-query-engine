# ⚡ Voice-to-SQL Query Engine

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://voice-to-sql-query-engine-web.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://voice-to-sql-query-engine-web.vercel.app](https://voice-to-sql-query-engine-web.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Natural language to SQL compiler with AST token sandboxing, table allowlisting, and mutation prevention to block unauthorized execution and injection attacks.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** sqlglot, sqlparse, FastAPI, SQLite
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **AST Validation:** Analyzes parsed token syntax trees using sqlglot to reject DROP, ALTER, and UPDATE queries.
* **Table Allowlist:** Blocks access to tables outside predefined database boundaries.
* **Parameterized Execution:** Raw string interpolation removed in favor of parameterized query bindings.

---

## 🚀 API Contracts
```http
POST /api/v1/sql/compile
Request:
{
  "prompt": "Show all orders over 500 dollars made by customers in the last 30 days"
}

Response (200 OK):
{
  "sql": "SELECT customer_id, order_total FROM orders WHERE order_total > 500;",
  "ast_valid": true,
  "tables_accessed": ["orders"],
  "security_tier": "READ_ONLY_AUTHORIZED"
}

GET /health
Response: {"status": "healthy"}
💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v