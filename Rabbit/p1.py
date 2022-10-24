#Este productor envía mensajes a las colas "x" y "y"
#Las colas x, y están creadas en RabbitMQ

import pika

conexion = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
canal = conexion.channel()

#El canal que se creó en Rabbitmq se llama "x". Se especifica en la routing_key de la siguiente línea
canal.basic_publish(exchange='', routing_key='x', body="Saludos")
#El canal que se creó en Rabbitmq se llama "y". Se especifica en la routing_key de la siguiente línea
canal.basic_publish(exchange='', routing_key='y', body="Buenos días")

print("Los mensajes se han enviado")
conexion.close()
