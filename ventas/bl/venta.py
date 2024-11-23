from repository.venta import (
    obtener_ventas,
    obtener_venta_por_id,
    crear_venta,
    actualizar_venta,
    eliminar_venta
)

def listar_ventas():
    return obtener_ventas()

def obtener_venta(id_venta: int):
    venta = obtener_venta_por_id(id_venta)
    if not venta:
        raise ValueError("La venta no existe.")
    return venta

def agregar_venta(venta_data):
    return crear_venta(venta_data)

def modificar_venta(id_venta: int, venta_data):
    if not obtener_venta_por_id(id_venta):
        raise ValueError("La venta no existe.")
    actualizar_venta(id_venta, venta_data)

def borrar_venta(id_venta: int):
    if not obtener_venta_por_id(id_venta):
        raise ValueError("La venta no existe.")
    eliminar_venta(id_venta)
