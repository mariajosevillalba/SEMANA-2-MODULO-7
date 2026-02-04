from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from users import users_db
from errors import error_401

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    if token not in users_db:
        error_401()

    return users_db[token]
