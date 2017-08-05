import os
import sys
import ijson
from html import unescape

import contextlib

from django.core.management.base import BaseCommand, CommandError
from core.models import Question

SAMPLE_PATH = 'core/data/sample.json'
DATA_PATH = 'core/data/jeopardy_questions.json'
DEFAULT_QUESTION_VALUE = '$1000'
ERROR_LOG_FILE = 'logs/import_data.error'

class Command(BaseCommand):
    help = 'Load questions into db from json file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--sample',
            action='store_true',
            default=False,
            help='Use sample data',
        )

    def get_error_log(self):
        os.makedirs('logs', exist_ok=True)

        with contextlib.suppress(FileNotFoundError):
            os.remove(ERROR_LOG_FILE)

        return open(ERROR_LOG_FILE, 'w+')

    def handle(self, *args, **kwargs):
        print(self.style.SUCCESS('Starting load task:'))

        data_path = DATA_PATH

        if kwargs['sample']:
            data_path = SAMPLE_PATH

        f = open(data_path)
        objects = ijson.items(f, 'item')

        log = self.get_error_log()

        was_error = False

        for o in objects:
            try:
                if not o['value']:
                    o['value'] = DEFAULT_QUESTION_VALUE

                Question.objects.create(
                    question=unescape(o['question']),
                    air_date=o['air_date'],
                    answer=unescape(o['answer']),
                    value=int(o['value'][1:].replace(',', '')),
                    round=o['round'],
                    show_number=o['show_number'],
                )
                print(self.style.SUCCESS('.'), sep=' ', end='', file=sys.stdout, flush=True)
            except Exception as e:
                print(self.style.ERROR('X'), sep=' ', end='', file=sys.stdout, flush=True)
                was_error = True
                log.write('{} - {}\n'.format(e, str(o)))
        if was_error:
            self.stdout.write('')
            raise CommandError('Error loading question data. Check logs/import_data.error for more details')
        else:
            self.stdout.write(self.style.SUCCESS('\nDone'))
        log.close()
        f.close()

