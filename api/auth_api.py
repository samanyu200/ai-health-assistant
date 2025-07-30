from fastapi import APIRouter, HTTPException, Form
from pydantic import BaseModel
from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta

SECRET = "super-secret-key"
router = APIRouter()

users_db = {}  # Use a real DB later

class AuthResponse(BaseModel):
    access_token: str
    token_type: str

def create_token(username: str):
    expire = datetime.utcnow() + timedelta(days=7)
    return jwt.encode({"sub": username, "exp": expire}, SECRET, algorithm="HS256")

@router.post("/register")
def register(username: str = Form(...), password: str = Form(...), confirm: str = Form(...)):
    if username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists.")
    if password != confirm:
        raise HTTPException(status_code=400, detail="Passwords do not match.")
    users_db[username] = bcrypt.hash(password)
    return {"message": "User registered successfully."}

@router.post("/login", response_model=AuthResponse)
def login(username: str = Form(...), password: str = Form(...)):
    if username not in users_db or not bcrypt.verify(password, users_db[username]):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    token = create_token(username)
    return {"access_token": token, "token_type": "bearer"}
