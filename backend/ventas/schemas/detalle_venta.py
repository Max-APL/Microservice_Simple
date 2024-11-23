from pydantic import BaseModel
from typing import Optional

class DetalleVentaBase(BaseModel):
    id_venta: int
    id_producto: int
    cantidad: int

class DetalleVentaCreate(DetalleVentaBase):
    """Esquema para la creación (entrada de datos)."""
    pass

class DetalleVentaProcessed(BaseModel):
    """Esquema interno después de agregar información del producto."""
    id_venta: int
    id_producto: int
    cantidad: int
    nombre_producto: Optional[str] = None
    precio_unitario: Optional[float] = None
    subtotal: Optional[float] = None

class DetalleVentaRead(DetalleVentaProcessed):
    id: int

    class Config:
        orm_mode = True
