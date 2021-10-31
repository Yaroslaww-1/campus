import _thread
import os
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
    # def run(self, *args, **options):
    #     if os.environ.get('RUN_MAIN') != 'true':
    #         self.stdout.write('About to start running')
    #         try:
    #             super(Command, self).run(**options)
    #         except Exception as e:
    #             _thread.interrupt_main()
    #             logging.exception("An exception was thrown!")
    #             raise

    def inner_run(self, *args, **options):
        try:
            super().inner_run(*args, **options)
        except Exception as e:
            _thread.interrupt_main()
            logging.exception("An exception was thrown!")
            raise
