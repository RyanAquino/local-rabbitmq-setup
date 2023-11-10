import pika

def callback(ch, method, properties, body):
    # Simulate message processing
    # ...

    # Acknowledge the message
    import time
    print("processing")
    # time.sleep(5)
    print(f"Consumer 1 received message: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume_messages():
    connection_params = pika.ConnectionParameters(
        host='localhost',
        port=5672,
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue='test-queue-q', durable=True, arguments={"x-queue-type": "quorum"})

    # Enable message acknowledgment
    channel.basic_consume(queue='test-queue-q', on_message_callback=callback, auto_ack=False)

    print('Consumer 1 waiting for messages. To exit, press Ctrl+C')
    channel.start_consuming()


if __name__ == "__main__":
    consume_messages()
