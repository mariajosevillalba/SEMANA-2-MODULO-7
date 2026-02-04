from fastapi import FastAPI, Depends
from security import get_current_user
from roles import ROLE_ADMIN
from errors import error_403

app = FastAPI()

# Ruta pública
@app.get("/")
def home():
    return {"mensaje": "API pública funcionando"}

# Ruta protegida (solo autenticación)
@app.get("/perfil")
def perfil(user: dict = Depends(get_current_user)):
    return {
        "id": user["id"],
        "usuario": user["username"],
        "rol": user["role"]
    }

# Ruta protegida + rol admin
@app.get("/admin")
def admin_panel(user: dict = Depends(get_current_user)):
    if user["role"] != ROLE_ADMIN:
        error_403()

    return {"mensaje": "Acceso permitido al administrador"}
