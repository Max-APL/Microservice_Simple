import pika

try:
    credentials = pika.PlainCredentials("manager", "1590rabbit")
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue="test_queue")
    print("Conexión exitosa a RabbitMQ")
    connection.close()
except Exception as e:
    print(f"Error al conectar a RabbitMQ: {e}")
