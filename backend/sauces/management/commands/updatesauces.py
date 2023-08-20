import grequests

from django.db import transaction
from django.db.models import Q, F, IntegerField
from django.db.models.functions import Cast
from django.core.management.base import BaseCommand, CommandError

from sauces.models import Sauce, Source
from sauces.sources import get_fetcher
from sauces.tasks import calc_hashes


class Command(BaseCommand):
    help = "Fetches new sauces for the specified fetcher/source"

    def add_arguments(self, parser):
        parser.add_argument("source", type=str)
        parser.add_argument("--start-from", type=str, default="last")
        parser.add_argument("--async-reqs", type=int, default=3)
        parser.add_argument("--calc-hashes", type=bool, default=False)

    def handle(self, *args, **options):
        fetcher_class = get_fetcher(options["source"].lower())

        if fetcher_class is None:
            raise CommandError(f"Invalid fetcher: {options['fetcher']}")

        fetcher = fetcher_class(
            async_reqs=options["async_reqs"],
        )
        source = fetcher.source

        start_from = options["start_from"]

        self.stdout.write(
            f"Fetching sauces from {source.name}"
            + (" (and calculating hashes)" if options["calc_hashes"] else "")
            + (f", starting from page {start_from}" if start_from else "")
        )

        for sauce in fetcher.get_sauces_iter(
            start_from=start_from
            if start_from and (start_from.isnumeric() or start_from[1:].isnumeric())
            else fetcher.last_sauce,
        ):
            self.stdout.write(
                self.style.SUCCESS(f"ADDED")
                + f": {sauce.source_site_id} - {sauce.title}"
            )
            if options["calc_hashes"]:
                calc_hashes.delay(sauce.id)
