import os


class RabbitMQOptions:
    def __init__(self):
        self.host_name = os.getenv('RABBITMQ_HOST_NAME')
        self.port = os.getenv('RABBITMQ_PORT')
        self.queue_name = os.getenv('RABBITMQ_QUEUE_NAME')
        self.broker_name = os.getenv('RABBITMQ_BROKER_NAME')
