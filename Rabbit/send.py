import pika

conexion = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
canal = conexion.channel()

#El canal que se creó en Rabbitmq se llama "cola". Se especifica en la routing_key de la siguiente línea

canal.basic_publish(exchange='', routing_key='cola', body="Saludos")

print("El mensaje se ha enviado")
conexion.close()