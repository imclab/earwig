import sys
from django.core import management
from django.core.management.base import BaseCommand, CommandError

from contact.testutils import create_test_attempt


class Command(BaseCommand):
    '''Generate
    '''
    args = '<output_filename>'

    fixture_functions = [
        create_test_attempt,
        ]

    def handle(self, output_filename, *args, **options):
        management.call_command('syncdb', database='test', verbosity=1)
        for func in self.fixture_functions:
            func()
        with open(output_filename, 'w') as f:
            management.call_command(
                'dumpdata', 'contact', indent=4, database='test', stdout=f)