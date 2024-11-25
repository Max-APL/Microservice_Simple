# config.py

DATABASE_CONFIG = {
    "host": "localhost",
    "database": "arqui_producto_db",
    "user": "root",
    "password": "",
    "pool_name": "producto_pool",
    "pool_size": 21  # Número de conexiones en el pool
}

RABBITMQ_CONFIG = {
    "host": "localhost",
    "user": "andy",
    "password": "a1234",
    "queue_request": "productos_request",
    "queue_response": "productos_response"
}