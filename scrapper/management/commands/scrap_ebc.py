from django.core.management.base import BaseCommand

from scrapper import services


class Command(BaseCommand):
    help = 'Gets data from EBC RSS feed'

    def handle(self, *args, **options):
        services.ScrapperService.save_latest_rates()

        self.stdout.write('Import finished')
