from fastapi import APIRouter, status
from app.schema.consulta import ConsultaCreate, ConsultaResponse
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=ConsultaResponse, status_code=status.HTTP_201_CREATED)
def crear_consulta(consultas: ConsultaCreate):
    # Aquí invocaremos al servicio o repositorio de Base de Datos
    consulta_guardada = {
        "id": 1,
        **consultas.model_dump(),
        "fecha_registro": datetime.now()
    }
    return consulta_guardada
