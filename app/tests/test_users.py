import pytest
import requests

DELETE_IDS = [5, 6]

GET_DATA = [
    {
        "id": 1,
        "email": "janet.weaver@fast.api",
        "first_name": "Janet",
        "last_name": "Weaver"
    },
    {
        "id": 2,
        "email": "andrew.green@fast.api",
        "first_name": "Andrew",
        "last_name": "Green"
    }
]

POST_DATA = [
    {
        "email": "testmail@google.com",
        "first_name": "Jacob",
        "last_name": "Baskin"
    },
    {
        "email": "number6@google.com",
        "first_name": "Nikolay",
        "last_name": "Prokhorov"
    }
]

PATCH_DATA = {
    5: {
        "email": "newmail@google.com",
        "first_name": "Robert",
        "last_name": "Roberts"
    }
}

def test_get_users_list(url: str):
    
    response = requests.get(f"{url}/api/users/")
    
    assert response.status_code == 200, \
        f"Ожидался статус 200, получен {response.status_code}"
    
    data = response.json()
    users_len = len(data["results"])
    assert users_len == 4, \
        f"Ожидалось 4 пользователя, получено {users_len}"

@pytest.mark.parametrize("user_data", GET_DATA)
def test_single_user_get(url: str, user_data: dict):
    
    user_id = user_data["id"]
    response = requests.get(f"{url}/api/users/{user_id}")
    
    assert response.status_code == 200, \
        f"Ожидался статус 200, получен {response.status_code}"
    
    result = response.json()["results"]
    assert result["id"] == user_id, \
        f"Ожидался id {user_id}, получен {result['id']}"
    
    assert result["email"] == user_data["email"], \
        f"Ожидался email {user_data['email']}, получен {result['email']}"

    assert result["first_name"] == user_data["first_name"], \
        f"Ожидалось имя {user_data['first_name']}, получено {result['first_name']}"
        
    assert result["last_name"] == user_data["last_name"], \
        f"Ожидалась фамилия {user_data['last_name']}, получена {result['last_name']}"        

@pytest.mark.parametrize("user_data", POST_DATA)
def test_users_create(url: str, user_data: dict):
    
    response = requests.post(f"{url}/api/users/", json=user_data)
    
    assert response.status_code == 200, \
        f"Ожидался статус 200, получен {response.status_code}"
        
    results = response.json()
    
    assert results["message"] == "User Created", \
        f"Ожидалось сообщение 'User Created', получено {results['message']}"
        
    assert results["results"]["email"] == user_data["email"], \
        f"Ожидался email {user_data['email']}, получен {results['results']['email']}"
        
    assert results["results"]["first_name"] == user_data["first_name"], \
        f"Ожидалось имя {user_data['first_name']}, получено {results['results']['first_name']}"
        
    assert results["results"]["last_name"] == user_data["last_name"], \
        f"Ожидалась фамилия {user_data['last_name']}, получена {results['results']['last_name']}"
      
def test_single_user_patch(url: str):
    
    user_id = list(PATCH_DATA.keys())[0]
    
    response = requests.patch(f"{url}/api/users/{user_id}", json=PATCH_DATA[user_id])
    
    assert response.status_code == 200, \
        f"Ожидался статус 200, получен {response.status_code}"
        
    results = response.json()
    
    assert results["message"] == "User Successfully Updated", \
        f"Ожидалось сообщение 'User Successfully Updated', получено {results['message']}"
        
    assert results["results"]["email"] == PATCH_DATA[user_id]["email"], \
        f"Ожидался email {PATCH_DATA[user_id]['email']}, получен {results['results']['email']}"
        
    assert results["results"]["first_name"] == PATCH_DATA[user_id]["first_name"], \
        f"Ожидалось имя {PATCH_DATA[user_id]['first_name']}, получено {results['results']['first_name']}"
        
    assert results["results"]["last_name"] == PATCH_DATA[user_id]["last_name"], \
        f"Ожидалась фамилия {PATCH_DATA[user_id]['last_name']}, получена {results['results']['last_name']}"
        
def test_users_delete(url: str):
    
    response = requests.delete(f"{url}/api/users/", json={"ids": DELETE_IDS})
    
    assert response.status_code == 200, \
        f"Ожидался статус 200, получен {response.status_code}"
        
    results = response.json()
    
    assert results["message"] == f"Users {DELETE_IDS} Successfully Deleted", \
        f"Ожидалось сообщение 'Users {DELETE_IDS} Successfully Deleted', получено {results['message']}"
    
    results_len = len(results["results"])
    assert results_len == 4, \
        f"Ожидалось 4 пользователя, получено {results_len}"
    