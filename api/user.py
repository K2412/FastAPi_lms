import fastapi
from pydantic import BaseModel
from typing import Optional, List
#router for app(similar to blue print in Flask)
router = fastapi.APIRouter()

users = []

class User(BaseModel):
# Required feilds 
    email: str
    is_active: bool
# Optional feilds
    bio: Optional[str]




# Pydantic to define response types/classes
@router.get("/users", response_model=List[User])
async def get_users():
    return users
# seperate function for each HTTP method
@router.post("/users")
# Data validation, validating that information being passed to the databas is appropriate
async def post_message(user: User):
    users.append(user)
    return 'success'


#Receive user infor by user id(path and query endpoints with data validation)

@router.get("/users/{id}")
async def get_users(id: int):
    return users[id]
