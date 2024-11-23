from fastapi import APIRouter, HTTPException
from bl.detalle_venta import (
    listar_detalles_venta,
    obtener_detalle_venta,
    agregar_detalle_venta,
    borrar_detalle_venta
)
from schemas.detalle_venta import DetalleVentaRead, DetalleVentaCreate

router = APIRouter()

@router.get("/detalle", response_model=list[DetalleVentaRead])
def get_detalles_venta():
    return listar_detalles_venta()

@router.get("/detalle/{id}", response_model=DetalleVentaRead)
def get_detalle_venta(id: int):
    try:
        return obtener_detalle_venta(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/detalle", response_model=DetalleVentaRead)
def create_detalle_venta(detalle: DetalleVentaCreate):
    try:
        detalle_id = agregar_detalle_venta(detalle)
        return obtener_detalle_venta(detalle_id)  # Consultamos para incluir todos los datos
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/detalle/{id}")
def delete_detalle_venta(id: int):
    try:
        borrar_detalle_venta(id)
        return {"detail": "Detalle de venta eliminado"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
