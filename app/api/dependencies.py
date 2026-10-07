# app/api/dependencies.py
from app.auth import get_current_user
from app.models.user import User
from fastapi import APIRouter, Depends, HTTPException, status


def require_role(role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have the required role to access this resource.",
            )
        return current_user

    return role_checker
