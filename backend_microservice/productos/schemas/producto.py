from pydantic import BaseModel
from typing import Optional

# Esquema base que contiene los atributos comunes
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str]
    precio: float
    id_categoria: int
    id_marca: int

# Esquema para creación (entrada de datos)
class ProductoCreate(ProductoBase):
    pass

# Esquema para respuesta tras creación (incluye ID)
class ProductoRead(ProductoBase):
    id_producto: int

    class Config:
        orm_mode = True
