#Este consumidor recibe los mensajes "y"

import pika, sys, os

def main():
    conexion = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    canal = conexion.channel()

    def callback(ch, method, properties, body):
        print(" [x] C2 ha recibido el mensaje %r" % body)
    
    canal.basic_consume(queue="y", on_message_callback= callback, auto_ack=True)
    canal.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrumpido")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
        