import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.api
def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    print(f"✅ Nombre d’utilisateurs : {len(data['data'])}")
