import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_safe_sql_generation():
    payload = {"query_text": "Show top 5 employees", "target_table": "employees"}
    res = client.post("/api/v1/sql/generate", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["is_safe"] is True
    assert "SELECT" in data["generated_sql"]
    assert "employees" in data["generated_sql"]

def test_sql_injection_rejection():
    payload = {"query_text": "DROP TABLE users;--", "target_table": "employees"}
    res = client.post("/api/v1/sql/generate", json=payload)
    assert res.status_code == 400

def test_invalid_table_whitelist_rejection():
    payload = {"query_text": "Show all records", "target_table": "unauthorized_table"}
    res = client.post("/api/v1/sql/generate", json=payload)
    assert res.status_code == 400
