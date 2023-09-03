from typing import Any, List
from fastapi.routing import APIRouter

from schemas.user_schemas import User

router = APIRouter()

@router.get('/', response_model=List[User])
def get_users() -> Any:
  return [
    {
      "name": "John",
      "age": 20
    }  
  ]

@router.post("/")
def create_user(user: User):
  '''
    Reference: Create a new user
    args: user
  '''
  return 