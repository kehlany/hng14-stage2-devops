from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

with patch('redis.Redis') as mock_redis:
    mock_r = MagicMock()
    mock_redis.return_value = mock_r
    from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_job():
    mock_r.lpush.return_value = 1
    mock_r.hset.return_value = 1
    response = client.post("/jobs")
    assert response.status_code == 200
    data = response.json()
    assert "job_id" in data

def test_get_job_found():
    mock_r.hget.return_value = b"queued"
    response = client.get("/jobs/test-id-123")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "queued"

def test_get_job_not_found():
    mock_r.hget.return_value = None
    response = client.get("/jobs/nonexistent-id")
    assert response.status_code == 200
    assert response.json() == {"error": "not found"}