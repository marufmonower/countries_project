import requests
from django.core.management.base import BaseCommand
from countries.models import Country


class Command (BaseCommand):
    help = 'Fetch countries data from REST API and save to database'

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch data"))
            return

        data = response.json()

        for item in data:
            country, created = Country.objects.update_or_create(
                name=item.get("name", {}).get("common"),
                defaults={
                    "official_name": item.get("name", {}).get("official"),
                    "capital": item.get("capital", [None])[0],
                    "region": item.get("region"),
                    "subregion": item.get("subregion"),
                    "population": item.get("population"),
                    "area": item.get("area"),
                    "flag_url": item.get("flags", {}).get("png"),
                    "independent": item.get("independent"),
                    "cca2": item.get("cca2"),
                    "cca3": item.get("cca3"),
                    "ccn3": item.get("ccn3"),
                    "currencies": item.get("currencies"),
                    "languages": item.get("languages"),
                }
            )

        self.stdout.write(self.style.SUCCESS(
            "Countries data fetched and stored successfully."))
