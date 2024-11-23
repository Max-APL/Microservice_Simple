import pika
import json
from core.config import RABBITMQ_CONFIG

class RabbitMQService:
    def __init__(self):
        credentials = pika.PlainCredentials(RABBITMQ_CONFIG["user"], RABBITMQ_CONFIG["password"])
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBITMQ_CONFIG["host"],
                credentials=credentials
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=RABBITMQ_CONFIG["queue_request"])
        self.channel.queue_declare(queue=RABBITMQ_CONFIG["queue_response"])

    def send_message(self, product_id):
        """Enviar mensaje solicitando información del producto."""
        message = {"id_producto": product_id}
        self.channel.basic_publish(
            exchange="",
            routing_key=RABBITMQ_CONFIG["queue_request"],
            body=json.dumps(message)
        )

    def receive_message(self):
        """Recibir respuesta del microservicio de productos."""
        for method_frame, properties, body in self.channel.consume(RABBITMQ_CONFIG["queue_response"]):
            self.channel.basic_ack(method_frame.delivery_tag)
            return json.loads(body)

    def close(self):
        """Cerrar conexión."""
        self.connection.close()
