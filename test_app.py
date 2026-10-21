from app import app
import pytest


@pytest.fixture
def client():
  app.config["TESTING"] = True
  with app.test_client() as client:
    yield client


def test_home(client):
  response = client.get("/")
  assert response.status_code == 200
  assert b"Welcome to the Flask CI/CD Demo API!" in response.data


def test_get_tasks(client):
  response = client.get("/tasks")
  assert response.status_code == 200
  assert isinstance(response.json, list)


def test_add_task(client):
  response = client.post("/tasks", json={"title": "Test automated deployment"})
  assert response.status_code == 201
  assert response.json["title"] == "Test automated deployment"
