from fastapi import FastAPI
from app.api.v1.endpoints import consultas

# Crear la instancia de la aplicación
app = FastAPI(
    title="API de Gestión de Consultas Médicas",
    version="1.0.0"
)

# Incluimos los módulos/rutas usando prefijos claros
app.include_router(consultas.router, prefix="/api/v1/consultas", tags=["Consultas Médicas"])

@app.get("/")
def root():
    return {"mensaje": "API Médica Operativa"}