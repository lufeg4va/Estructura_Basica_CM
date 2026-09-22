from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Crear la instancia de la aplicación
app = FastAPI(
    title="API de Gestión de Consultas Médicas",
    version="1.0.0"
)

# Modelo Pydantic para validar los datos de entrada de una consulta
class ConsultaMedica(BaseModel):
    paciente_id: int
    motivo_consulta: str
    diagnostico: str
    receta_notas: Optional[str] = None

# Ruta de prueba
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al Backend del Consultorio Médico"}

# Endpoint POST para registrar una nueva consulta
@app.post("/consultas/")
def registrar_consulta(consulta: ConsultaMedica):
    # Aquí iría la lógica para guardar en la Base de Datos
    return {
        "estado": "Consulta registrada exitosamente",
        "fecha_registro": datetime.now(),
        "datos": consulta
    }
