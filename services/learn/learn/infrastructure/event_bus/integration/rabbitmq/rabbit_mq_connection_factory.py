import inject
import pika
from pika.adapters.blocking_connection import BlockingChannel

from learn.api.options.rabbit_mq_options import RabbitMQOptions


class RabbitMQConnectionFactory:
    @inject.autoparams()
    def __init__(self, options: RabbitMQOptions):
        self._options = options
        import logging
        logging.basicConfig()
        print(options.host_name, options.port)
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=options.host_name, port=options.port, connection_attempts=5))

    @property
    def connection(self):
        return self._connection

    @property
    def broker_name(self):
        return self._options.broker_name

    @property
    def queue_name(self):
        return self._options.queue_name
