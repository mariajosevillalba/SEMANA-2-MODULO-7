from fastapi import HTTPException, status

def error_401():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autenticado"
    )

def error_403():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="No autorizado"
    )
