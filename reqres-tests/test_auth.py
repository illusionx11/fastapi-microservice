import pytest
import requests

REG_MOCK_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

LOGIN_MOCK_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

AUTH_TOKEN = "QpwL5tke4Pnpja7X4"

def test_register(base_url: str):
    
    response = requests.post(f"{base_url}/register", json=REG_MOCK_DATA)
    
    assert response.status_code == 200, \
        f"Ожидался статус 200, получен {response.status_code}"
    
    result = response.json()
    
    assert result["id"] == 4, \
        f"Ожидался id 4, получен {result['id']}"
    
    assert result["token"] == AUTH_TOKEN, \
        f"Ожидался токен регистрации {AUTH_TOKEN}, получен {result['token']}"

def test_login(base_url: str):
    
    response = requests.post(f"{base_url}/login", json=LOGIN_MOCK_DATA)
    
    assert response.status_code == 200, \
        f"Ожидался статус 200, получен {response.status_code}"
    
    result = response.json()
    
    assert result["token"] == AUTH_TOKEN, \
        f"Ожидался токен регистрации {AUTH_TOKEN}, получен {result['token']}"