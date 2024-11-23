from fastapi import APIRouter, HTTPException
from bl.venta import (
    listar_ventas,
    obtener_venta,
    agregar_venta,
    modificar_venta,
    borrar_venta
)
from schemas.venta import VentaRead, VentaCreate

router = APIRouter()

@router.get("/venta", response_model=list[VentaRead])
def get_ventas():
    return listar_ventas()

@router.get("/venta/{id_venta}", response_model=VentaRead)
def get_venta(id_venta: int):
    try:
        return obtener_venta(id_venta)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/venta", response_model=VentaRead)
def create_venta(venta: VentaCreate):
    venta_id = agregar_venta(venta)
    return VentaRead(id_venta=venta_id, **venta.dict())

@router.put("/venta/{id_venta}", response_model=VentaRead)
def update_venta(id_venta: int, venta: VentaCreate):
    try:
        modificar_venta(id_venta, venta)
        return VentaRead(id_venta=id_venta, **venta.dict())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/venta/{id_venta}")
def delete_venta(id_venta: int):
    try:
        borrar_venta(id_venta)
        return {"detail": "Venta eliminada"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
