from django.core.management.base import BaseCommand
from myapp.models import KickStarter
import csv

class Command(BaseCommand):
    help = 'imports data from csv'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Path to CSV to load')

    def handle(self, *args, **kwargs):
        # Iterate through CSV and load row into model
        file_path = kwargs['path']

        # Reading a CSV
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #skip the first row
                if(line_count != 0):
                    KickStarter.objects.create(
                        backers_count = row[0],
                        blurb = row[1],
                        category = row[2],
                        converted_pledged_amount = row[3]
                        )
                line_count += 1
            