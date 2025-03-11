import json
import os

USERS_PATH = f"{os.getcwd()}/data/users.json"

def load_users() -> list[dict]:
    with open(USERS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(data: list[dict]) -> None:
    with open(USERS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)