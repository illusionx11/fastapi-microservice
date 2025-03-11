from fastapi import FastAPI, HTTPException
from models.models import UserData
from data.utils import load_users, save_users
import json
import os

app = FastAPI()

@app.get("/api/users/")
async def list_users():
    
    users_list = load_users()
        
    try:
        return {"results": users_list}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error getting users list: {str(e)}")

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    
    users_list = load_users()
        
    try:
        user_data = next((u for u in users_list if u["id"] == user_id), None)
        
        if user_data:
            return {"results": user_data}
        
        else:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist.")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error getting user with id {user_id}: {str(e)}")

@app.post("/api/users/")
async def create_user(user_data: UserData):
    
    users_list = load_users()
    
    try:
        last_user_id = users_list[-1]["id"]
        new_user_data = {
            "id": last_user_id + 1,
            "email": user_data.email,
            "first_name": user_data.first_name,
            "last_name": user_data.last_name
        }
        
        users_list.append(new_user_data)

        save_users(users_list)
        
        return {"message": "User Created", "results": new_user_data}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating new user: {str(e)}")
    
@app.patch("/api/users/{user_id}")
async def patch_user(user_id: int, user_data: UserData):
    
    users_list = load_users()
        
    try:
        index = next((i for i, u in enumerate(users_list) if u["id"] == user_id), None)
        
        if index:
            users_list[index]["email"] = user_data.email
            users_list[index]["first_name"] = user_data.first_name
            users_list[index]["last_name"] = user_data.last_name
            
            save_users(users_list)
            users_list = load_users()
            return {"message": "User Successfully Updated", "results": users_list[index]}
        
        else:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist.")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating user with id {user_id}: {str(e)}")
    
@app.delete("/api/users/")
async def delete_user(user_ids: dict):
    
    users_list = load_users()
        
    try:
        
        for user_id in user_ids["ids"]:
            user = next((u for u in users_list if u["id"] == user_id), None)
            
            if user:
                users_list.remove(user)
                
                save_users(users_list)
            
            else:
                raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist.")
            
        users_list = load_users()
        return {"message": f"Users {user_ids['ids']} Successfully Deleted", "results": users_list}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting user with id {user_id}: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)