from repository.detalle_venta import (
    obtener_detalles_venta,
    obtener_detalle_venta_por_id,
    crear_detalle_venta,
    eliminar_detalle_venta
)
from services.rabbitmq_service import RabbitMQService
from schemas.detalle_venta import DetalleVentaCreate, DetalleVentaProcessed


def listar_detalles_venta():
    return obtener_detalles_venta()

def obtener_detalle_venta(id: int):
    detalle = obtener_detalle_venta_por_id(id)
    if not detalle:
        raise ValueError("El detalle de venta no existe.")
    return detalle

def agregar_detalle_venta(detalle_data: DetalleVentaCreate):
    # Inicializamos el esquema procesado
    detalle = DetalleVentaProcessed(
        id_venta=detalle_data.id_venta,
        id_producto=detalle_data.id_producto,
        cantidad=detalle_data.cantidad
    )

    # Conectarse a RabbitMQ para solicitar información del producto
    rabbitmq = RabbitMQService()
    rabbitmq.send_message(detalle.id_producto)
    product_info = rabbitmq.receive_message()
    rabbitmq.close()

    # Agregar la información del producto al detalle
    detalle.nombre_producto = product_info["nombre"]
    detalle.precio_unitario = product_info["precio"]
    detalle.subtotal = detalle.precio_unitario * detalle.cantidad

    # Crear el detalle de venta en la base de datos
    return crear_detalle_venta(detalle)

def borrar_detalle_venta(id: int):
    if not obtener_detalle_venta_por_id(id):
        raise ValueError("El detalle de venta no existe.")
    eliminar_detalle_venta(id)
