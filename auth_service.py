from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Auth Service")

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(req: LoginRequest):
    if req.username == "admin" and req.password == "admin":
        return {"token": "valid_token_12345"}
    raise HTTPException(status_code=401, detail="Unauthorized")