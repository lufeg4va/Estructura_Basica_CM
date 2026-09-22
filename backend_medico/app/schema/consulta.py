from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ConsultaBase(BaseModel):
    paciente_id: int
    motivo_consulta: str
    diagnostico: str
    receta_notas: Optional[str] = None

class ConsultaCreate(ConsultaBase):
    pass  # Hereda los campos necesarios para crear una consulta

class ConsultaResponse(ConsultaBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True 