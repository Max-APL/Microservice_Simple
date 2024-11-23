from pydantic import BaseModel
from typing import List
from datetime import date

# Esquema base para atributos comunes
class VentaBase(BaseModel):
    id_cliente: int
    fecha: date  # Seguimos usando `date` para la validación interna
    total: float

# Esquema para creación (entrada de datos)
class VentaCreate(VentaBase):
    pass

# Esquema para respuesta con ID
class VentaRead(VentaBase):
    id_venta: int

    class Config:
        orm_mode = True

        # Convierte `date` a cadena durante la serialización de la respuesta
        json_encoders = {
            date: lambda v: v.strftime("%Y-%m-%d")  # Formato de fecha "YYYY-MM-DD"
        }
