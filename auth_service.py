from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import setup_logging

app = FastAPI(title="Auth Service")
logger = setup_logging("auth_service")

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(req: LoginRequest):
    # Dummy login process
    logger.info("- Log in")
    if req.username == "admin" and req.password == "admin":
        logger.info("Log in sucessfull")
        return {"token": "valid_token_12345"}
    raise HTTPException(status_code=401, detail="Unauthorized")