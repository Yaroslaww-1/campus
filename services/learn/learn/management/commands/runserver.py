import _thread
import signal
import sys
import logging


from django.core.management.commands.runserver import Command as RunServer


def quit(*args):
    print('Quit app')
    sys.exit(1)


signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)


class Command(RunServer):
    def inner_run(self, *args, **options):
        try:
            super().inner_run(*args, **options)
        except Exception as e:
            _thread.interrupt_main()
            logging.exception("An exception was thrown!")
            raise
