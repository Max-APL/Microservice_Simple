from repository.producto import (
    obtener_productos,
    obtener_producto_por_id,
    crear_producto,
    actualizar_producto,
    eliminar_producto
)

from repository.producto import buscar_producto_por_id

def listar_productos():
    return obtener_productos()

def obtener_producto(id_producto: int):
    producto = obtener_producto_por_id(id_producto)
    if not producto:
        raise ValueError("El producto no existe.")
    return producto

def agregar_producto(producto_data):
    return crear_producto(producto_data)

def modificar_producto(id_producto: int, producto_data):
    if not obtener_producto_por_id(id_producto):
        raise ValueError("El producto no existe.")
    actualizar_producto(id_producto, producto_data)

def borrar_producto(id_producto: int):
    if not obtener_producto_por_id(id_producto):
        raise ValueError("El producto no existe.")
    eliminar_producto(id_producto)


def obtener_producto_por_id(id_producto):
    """Lógica para obtener un producto por su ID."""
    return buscar_producto_por_id(id_producto)