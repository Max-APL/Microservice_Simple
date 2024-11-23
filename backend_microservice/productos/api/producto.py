from fastapi import APIRouter, HTTPException
from bl.producto import (
    listar_productos,
    obtener_producto,
    agregar_producto,
    modificar_producto,
    borrar_producto,
)
from schemas.producto import ProductoRead, ProductoCreate

router = APIRouter()

@router.get("/productos", response_model=list[ProductoRead])
def get_productos():
    return listar_productos()

@router.get("/productos/{id_producto}", response_model=ProductoRead)
def get_producto(id_producto: int):
    try:
        return obtener_producto(id_producto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/productos", response_model=ProductoRead)
def create_producto(producto: ProductoCreate):
    producto_id = agregar_producto(producto)
    return ProductoRead(id_producto=producto_id, **producto.dict())

@router.put("/productos/{id_producto}", response_model=ProductoRead)
def update_producto(id_producto: int, producto: ProductoCreate):
    try:
        modificar_producto(id_producto, producto)
        return ProductoRead(id_producto=id_producto, **producto.dict())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/productos/{id_producto}")
def delete_producto(id_producto: int):
    try:
        borrar_producto(id_producto)
        return {"detail": "Producto eliminado"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
