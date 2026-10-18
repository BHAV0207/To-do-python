from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    assert client.get("/").status_code == 200


def test_healthz():
    assert client.get("/healthz").json()["status"] == "ok"


def test_metrics():
    assert "http_requests_total" in client.get("/metrics").text
