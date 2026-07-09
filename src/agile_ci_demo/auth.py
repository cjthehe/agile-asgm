from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4

router = APIRouter()

patients = {"patient@example.com": {"password": "password123", "name": "John Doe"}}

sessions: dict[str, str] = {}


class LoginRequest(BaseModel):
    email: str
    password: str


class LogoutRequest(BaseModel):
    session_id: str


@router.post("/login")
def login(login_data: LoginRequest):

    if login_data.email not in patients:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if patients[login_data.email]["password"] != login_data.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    session_id = str(uuid4())
    sessions[session_id] = login_data.email

    return {"message": "Login successful", "session_id": session_id}


@router.post("/logout")
def logout(logout_data: LogoutRequest):

    if logout_data.session_id not in sessions:
        raise HTTPException(status_code=401, detail="Invalid session")

    del sessions[logout_data.session_id]

    return {"message": "Logout successful", "redirect": "/login"}
