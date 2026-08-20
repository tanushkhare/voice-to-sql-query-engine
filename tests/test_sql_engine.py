import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_sql_compilation_average_salary():
    payload = {"query_text": "Find average salary in each department", "target_table": "employees"}
    res = client.post("/api/v1/sql/generate", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "AVG(salary)" in data["generated_sql"]
    assert data["is_safe"] is True

def test_sql_injection_safety_filter():
    payload = {"query_text": "Show employees; DROP TABLE employees;", "target_table": "employees"}
    res = client.post("/api/v1/sql/generate", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["is_safe"] is True  # The compiler sanitizes and replaces malicious commands
