from pydantic import BaseModel

class UserData(BaseModel):
    email: str
    first_name: str
    last_name: str
    
class UserResponse(BaseModel):
    data: UserData