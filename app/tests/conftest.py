import pytest
from ..data.utils import load_users, save_users

@pytest.fixture
def url():
    return "http://localhost:8000"

# очистить созданных тестом пользователей, оставить только моковые
@pytest.fixture(scope="session", autouse=True)
def delete_new_users():
    
    users_list = load_users()
    if len(users_list) > 4:
        users_list = users_list[:5]
        save_users(users_list)
    
    