from fastapi import FastAPI
from api.api import router as api_router
from db.db import engine

from db.models.user import User, Base

app = FastAPI()

@app.get("/")
def root():
  return {
      "version": "1.0.0"
  }

app.include_router(router=api_router)

@app.on_event("startup")
def startup():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)
  # session.commit()
  # session.close()