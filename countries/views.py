from django.shortcuts import render
from rest_framework import viewsets,filters
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
    
    @action(detail=True,methods=['get'])
    
    def same_region(self,request,pk=None):
        country = self.get_object()
        same_region_countries = Country.objects.filter(region=country.region).exclude(pk=country.pk)
        serializer = self.get_serializer(same_region_countries,many=True)
    
    @action(detail=False,methods=['get'],url_path='by-language/(?P<lang>\w+)')
    
    def by_language(self,request,lang=None):
        countries = Country.objects.filter(languages__icontains=lang)
        serializer = self.get_serializer(countries,many=True)
        return Response(serializer.data)
    
        
