import asyncio
import json
import logging
from typing import TypeVar
import humps
import threading
import inject
from pika import spec
from pika.adapters.blocking_connection import BlockingChannel
from apscheduler.schedulers.background import BackgroundScheduler


from learn.infrastructure.event_bus.integration.integration_event_bus import IntegrationEventBus
from learn.infrastructure.event_bus.integration.integration_event_handler import IntegrationEventHandler
from learn.infrastructure.event_bus.integration.rabbitmq.rabbit_mq_connection_factory import RabbitMQConnectionFactory


E = TypeVar('E')


class RabbitMQIntegrationEventBus(IntegrationEventBus):
    @inject.autoparams()
    def __init__(self, connection_factory: RabbitMQConnectionFactory):
        self._connection_factory = connection_factory
        self._consumer_channel = self._create_consumer_channel()

    def _create_consumer_channel(self) -> BlockingChannel:
        channel = self._connection_factory.connection.channel()

        channel.exchange_declare(
            exchange=self._connection_factory.broker_name,
            exchange_type='direct'
        )

        channel.queue_declare(
            queue=self._connection_factory.queue_name,
            durable=True,
            exclusive=False,
            auto_delete=False
        )

        channel.basic_qos(prefetch_count=1)

        return channel

    def subscribe(self, event_type: str):
        self._consumer_channel.queue_bind(
            queue=self._connection_factory.queue_name,
            exchange=self._connection_factory.broker_name,
            routing_key=event_type
        )

    def _start_consuming(self):
        self._consumer_channel.basic_consume(
            queue=self._connection_factory.queue_name,
            auto_ack=False,
            on_message_callback=self._process_integration_event
        )

        self._consumer_channel.start_consuming()
        # a = self._consumer_channel.consume(
        #     queue=self._connection_factory.queue_name,
        # )

    def _process_integration_events(self):
        print("processing integration events")
        self._connection_factory.connection.process_data_events()

    def start_consuming(self):
        # consumer_thread = threading.Thread(target=self._start_consuming)
        # consumer_thread.start()
        self._consumer_channel.basic_consume(
            queue=self._connection_factory.queue_name,
            auto_ack=False,
            on_message_callback=self._process_integration_event
        )

        queue_polling_job = BackgroundScheduler()
        queue_polling_job.add_job(self._process_integration_events, 'interval', seconds=10)
        queue_polling_job.start()

        # self._consumer_channel.start_consuming()

    # def start_consuming(self):
    #     self._consumer_channel.basic_consume(
    #         queue=self._connection_factory.queue_name,
    #         auto_ack=False,
    #         on_message_callback=self._process_integration_event
    #     )
    #
        # queue_polling_job = threading.Timer(10.0, self._fetch_and_process_integration_events)
        # queue_polling_job.start()
        # self._consumer_channel.start_consuming()

    def _process_integration_event(self, ch, method: spec.Basic.Deliver, properties: spec.BasicProperties, body: bytes):
        try:
            event_type = method.routing_key
            event = humps.depascalize(json.loads(body.decode("utf-8", "ignore")))
            print(f"start processing integration event, {event}")
            injector = inject.get_injector()
            handler = injector.get_instance(IntegrationEventHandler[event_type])
            handler.handle(event)
            self._consumer_channel.basic_ack(delivery_tag=method.delivery_tag, multiple=False)
            print(f"end processing integration event, {event}")
        except Exception as e:
            print(f"exception during integration event processing {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._connection_factory.connection.close()


# class RabbitMQIntegrationEventBusStarter:
#     def __init__(self, event_bus: RabbitMQIntegrationEventBus):
#         self._event_bus = event_bus
#
#     def start(self):
#         consumer_thread = threading.Thread(target=self._event_bus._start_consuming)
#         consumer_thread.start()


