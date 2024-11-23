from fastapi import APIRouter, HTTPException
from bl.marca import (
    listar_marcas,
    obtener_marca,
    agregar_marca,
    modificar_marca,
    borrar_marca
)
from schemas.marca import MarcaRead, MarcaCreate

router = APIRouter()

@router.get("/marcas", response_model=list[MarcaRead])
def get_marcas():
    return listar_marcas()

@router.get("/marcas/{id_marca}", response_model=MarcaRead)
def get_marca(id_marca: int):
    try:
        return obtener_marca(id_marca)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/marcas", response_model=MarcaRead)
def create_marca(marca: MarcaCreate):
    marca_id = agregar_marca(marca)
    return MarcaRead(id_marca=marca_id, **marca.dict())

@router.put("/marcas/{id_marca}", response_model=MarcaRead)
def update_marca(id_marca: int, marca: MarcaCreate):
    try:
        modificar_marca(id_marca, marca)
        return MarcaRead(id_marca=id_marca, **marca.dict())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/marcas/{id_marca}")
def delete_marca(id_marca: int):
    try:
        borrar_marca(id_marca)
        return {"detail": "Marca eliminada"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
