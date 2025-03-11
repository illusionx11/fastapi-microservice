import pytest
import requests

MOCK_DATA = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}

def test_single_user(base_url: str):
    
    user_id = MOCK_DATA["data"]["id"]
    response = requests.get(f"{base_url}/users/{user_id}")
    
    assert response.status_code == 200, \
        f"Ожидался статус 200, получен {response.status_code}"
    
    result = response.json()
    
    for key in ["id", "email", "first_name", "last_name", "avatar"]:
        assert result["data"][key] == MOCK_DATA["data"][key], \
            f"Ожидался data {key} {MOCK_DATA["data"][key]}, получен {result['data'][key]}"

    for key in ["url", "text"]:
        assert result["support"][key] == MOCK_DATA["support"][key], \
            f"Ожидался support {key} {MOCK_DATA["support"][key]}, получен {result['support'][key]}"  


