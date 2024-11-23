from repository.marca import (
    obtener_marcas,
    obtener_marca_por_id,
    crear_marca,
    actualizar_marca,
    eliminar_marca
)

def listar_marcas():
    return obtener_marcas()

def obtener_marca(id_marca: int):
    marca = obtener_marca_por_id(id_marca)
    if not marca:
        raise ValueError("La marca no existe.")
    return marca

def agregar_marca(marca_data):
    return crear_marca(marca_data)

def modificar_marca(id_marca: int, marca_data):
    if not obtener_marca_por_id(id_marca):
        raise ValueError("La marca no existe.")
    actualizar_marca(id_marca, marca_data)

def borrar_marca(id_marca: int):
    if not obtener_marca_por_id(id_marca):
        raise ValueError("La marca no existe.")
    eliminar_marca(id_marca)
