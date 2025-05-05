from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Country
from .serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def same_region(self, request, pk=None):
        country = self.get_object()
        same_region_countries = Country.objects.filter(
            region=country.region).exclude(pk=country.pk)
        serializer = self.get_serializer(same_region_countries, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='by-language/(?P<lang>\w+)')
    def by_language(self, request, lang=None):
        countries = Country.objects.filter(languages__icontains=lang)
        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)


def country_list(request):
    search_query = request.GET.get('search', '')
    countries = Country.objects.all()

    if search_query:
        countries = countries.filter(name__icontains=search_query)

    return render(request, 'countries/country_list.html', {'countries': countries})


def country_details(request, pk):

    country = get_object_or_404(Country, pk=pk)
    same_region = Country.objects.filter(
        region=country.region).exclude(pk=country.pk)
    languages = country.languages.split(',')#.all()
    return render(request, 'countries/country_details.html', {
        'country': country,
        'same_region': same_region,
        'languages': languages,
    })
