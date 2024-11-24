from repository.detalle_venta import (
    obtener_detalles_venta,
    obtener_detalle_venta_por_id,
    crear_detalle_venta,
    eliminar_detalle_venta,
    actualizar_detalle_venta_db
)
from services.rabbitmq_service import RabbitMQService
from schemas.detalle_venta import DetalleVentaCreate, DetalleVentaProcessed, DetalleVentaUpdate


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

def actualizar_detalle_venta(id_detalle: int, detalle_data: DetalleVentaUpdate):
    """Actualiza un detalle de venta después de validar el producto."""
    if detalle_data.id_producto:
        # Consultar el microservicio de Productos para obtener la información del producto
        rabbitmq = RabbitMQService()
        rabbitmq.send_message(detalle_data.id_producto)
        product_info = rabbitmq.receive_message()
        rabbitmq.close()

        if "error" in product_info:
            raise ValueError(f"Producto con ID {detalle_data.id_producto} no encontrado")

        # Agregar datos del producto al detalle
        detalle_data.nombre_producto = product_info["nombre"]
        detalle_data.precio_unitario = product_info["precio"]
        if detalle_data.cantidad is not None:
            detalle_data.subtotal = product_info["precio"] * detalle_data.cantidad

    # Actualizar el registro en la base de datos
    actualizar_detalle_venta_db(id_detalle, detalle_data)

    # Devolver el detalle actualizado
    return obtener_detalle_venta(id_detalle)
