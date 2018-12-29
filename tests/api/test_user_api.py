import pytest
from flask.wrappers import Response

@pytest.mark.useFixtures("client")
class TestUserApi:
  def test_create(self, client):
    rv: Response = client.post("/user", json={
      "method": "create",
      "param": {
        "email": "test_client@test.com"
      }
    })
    assert rv.status_code == 201

  def test_destroy(self, client):
    rv: Response = client.post("/user", json={
      "method": "destroy",
      "param": {
        "email": "test_client@test.com"
      }
    })
    assert rv.status_code == 200
    rv: Response = client.post("/user", json={
      "method": "show",
      "param": {
        "email": "test_client@test.com"
      }
    })
    assert rv.status_code == 404