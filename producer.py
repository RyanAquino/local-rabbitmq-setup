import pika


def publish_message(message, queue_name="test-queue-q"):
    # Establish a connection to the RabbitMQ server
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost", port=5672)
    )

    # Create a channel
    channel = connection.channel()

    # Declare a queue (create it if it doesn't exist)
    channel.queue_declare(
        queue=queue_name, durable=True, arguments={"x-queue-type": "quorum"}
    )

    # Publish the message to the queue
    for i in range(100000):
        channel.basic_publish(
            exchange="test-exchange-d",
            routing_key="test",
            body=f"{message} {i}",
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make the message persistent
            ),
        )

    print(f" [x] Sent '{message}' to '{queue_name}'")

    # Close the connection
    connection.close()


# Example usage
if __name__ == "__main__":
    message_to_send = "Hello, RabbitMQ!"
    publish_message(message_to_send, queue_name="test-queue-q")
