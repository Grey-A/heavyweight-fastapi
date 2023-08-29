from fastapi import status, HTTPException

InvalidTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate token",
    headers={"WWW-Authenticate": "Bearer"},
)
