#Este productor envía mensajes a la cola "y"
#La cola y está creada en RabbitMQ

import pika

conexion = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
canal = conexion.channel()

#El canal que se creó en Rabbitmq se llama "y". Se especifica en la routing_key de la siguiente línea

canal.basic_publish(exchange='', routing_key='y', body="Buenos días")
print("El mensaje se ha enviado")
conexion.close()
