import csv
from django.core.management.base import BaseCommand, CommandParser
from Userapp.models import Price

class Command(BaseCommand):

    def add_arguments(self, parser) -> None:
        parser.add_argument('csv_file',type=str ,help='path')

    def handle(self,*args,**kwargs):
        filepath = kwargs['csv_file']
        with open(filepath,'r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                Price.objects.create(
                    id = i['id'],
                    price = i['price'],
                    open = i['open'],
                    high = i['high'],
                    low = i['low'],
                    volume = i['volume'],
                    price_diff = i['price_diff'],
                    change = i['change'],
                    date = i['date'],
                    company_id = i['company_id'],
                    symbol = i['symbol'],
                )
        self.stdout.write(self.style.SUCCESS("Updates Done"))