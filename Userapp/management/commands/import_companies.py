import csv
from django.core.management.base import BaseCommand
from Userapp.models import Company

class Command(BaseCommand):
    help = 'Import companies from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Company.objects.create(
                    company_name=row['company_name'],
                    symbol=row['symbol'],
                    scripcode=row['scripcode']
                )
        self.stdout.write(self.style.SUCCESS('Companies imported successfully!'))