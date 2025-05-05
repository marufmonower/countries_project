from django.db import models


class Country (models.Model):
    name = models.CharField(max_length=255)
    official_name = models.CharField(max_length=255, null=True, blank=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    flag_url = models.URLField(null=True, blank=True)
    independent = models.BooleanField(null=True)
    cca2 = models.CharField(max_length=5, null=True, blank=True)
    cca3 = models.CharField(max_length=5, null=True, blank=True)
    ccn3 = models.CharField(max_length=5, null=True, blank=True)
    currencies = models.JSONField(null=True, blank=True)
    languages = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
