from fastapi import APIRouter, HTTPException
from bl.categoria import (
    listar_categorias,
    obtener_categoria,
    agregar_categoria,
    modificar_categoria,
    borrar_categoria
)
from schemas.categoria import CategoriaRead, CategoriaCreate

router = APIRouter()

@router.get("/categorias", response_model=list[CategoriaRead])
def get_categorias():
    return listar_categorias()

@router.get("/categorias/{id_categoria}", response_model=CategoriaRead)
def get_categoria(id_categoria: int):
    try:
        return obtener_categoria(id_categoria)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/categorias", response_model=CategoriaRead)
def create_categoria(categoria: CategoriaCreate):
    categoria_id = agregar_categoria(categoria)
    return CategoriaRead(id_categoria=categoria_id, **categoria.dict())

@router.put("/categorias/{id_categoria}", response_model=CategoriaRead)
def update_categoria(id_categoria: int, categoria: CategoriaCreate):
    try:
        modificar_categoria(id_categoria, categoria)
        return CategoriaRead(id_categoria=id_categoria, **categoria.dict())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/categorias/{id_categoria}")
def delete_categoria(id_categoria: int):
    try:
        borrar_categoria(id_categoria)
        return {"detail": "Categoría eliminada"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
