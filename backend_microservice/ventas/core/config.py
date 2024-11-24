# config.py

DATABASE_CONFIG = {
    "host": "localhost",
    "database": "arqui_venta_db",
    "user": "root",
    "password": "",
    "pool_name": "ventas_pool",
    "pool_size": 21  # Número de conexiones en el pool
}
# Configuración para RabbitMQ
RABBITMQ_CONFIG = {
    "host": "localhost",
    "queue_request": "productos_request",
    "queue_response": "productos_response",
    "user": "andy",
    "password": "a1234"
}