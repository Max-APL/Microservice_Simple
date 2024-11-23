from decimal import Decimal

import pika
import json
from threading import Thread
from core.config import RABBITMQ_CONFIG
from bl.producto import obtener_producto_por_id

def decimal_to_float(obj):
    """Convierte objetos Decimal a float para JSON serializable."""
    if isinstance(obj, dict):
        return {k: decimal_to_float(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [decimal_to_float(i) for i in obj]
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        return obj

def callback(ch, method, properties, body):
    """Callback que procesa los mensajes en productos_request."""
    print("Mensaje recibido:", body)
    message = json.loads(body)
    product_id = message.get("id_producto")

    producto = obtener_producto_por_id(product_id)
    if producto:
        response_message = {
            "id_producto": producto["id_producto"],
            "nombre": producto["nombre"],
            "precio": producto["precio"]
        }
    else:
        response_message = {"error": f"Producto con ID {product_id} no encontrado"}

    response_message = decimal_to_float(response_message)

    ch.basic_publish(
        exchange="",
        routing_key=RABBITMQ_CONFIG["queue_response"],
        body=json.dumps(response_message)
    )
    print(f"Respuesta enviada: {response_message}")

def start_rabbitmq_consumer():
    """Inicia el consumidor RabbitMQ en el hilo principal."""
    credentials = pika.PlainCredentials(RABBITMQ_CONFIG["user"], RABBITMQ_CONFIG["password"])
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_CONFIG["host"],
            credentials=credentials
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_CONFIG["queue_request"])
    channel.queue_declare(queue=RABBITMQ_CONFIG["queue_response"])
    channel.basic_consume(
        queue=RABBITMQ_CONFIG["queue_request"],
        on_message_callback=callback,
        auto_ack=True
    )
    print("Esperando mensajes en productos_request...")
    channel.start_consuming()

def run_consumer_in_thread():
    """Ejecuta el consumidor en un hilo separado."""
    thread = Thread(target=start_rabbitmq_consumer)
    thread.daemon = True  # Finaliza el hilo al cerrar el programa principal
    thread.start()
