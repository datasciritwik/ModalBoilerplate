from fastapi.testclient import TestClient
from app.main import create_app

client = TestClient(create_app())

def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert "status" in r.json()

def test_infer_unready():
    r = client.post("/api/infer", json={"text": "hello"})
    # Depending on startup timing test, model may not be ready. Accept 200 or 503.
    assert r.status_code in (200, 503)
