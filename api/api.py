from fastapi.routing import APIRouter

from api.endpoints import (
  users
)

router = APIRouter()

router.include_router(router=users.router, prefix='/users')