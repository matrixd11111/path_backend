from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .api.serializers import *


class SectionListView(ListAPIView):
    queryset = SectionModel.objects.all()
    serializer_class = SectionSerializer


class ThemeListView(ListAPIView):
    serializer_class = ThemeSerializer

    def get_queryset(self):
        return ThemeModel.objects.filter(section=self.kwargs.get('pk'))


class PablicationView(ListAPIView):
    serializer_class = PablicationSerializer

    def get_queryset(self):
        return PablicationModel.objects.filter(theme=self.kwargs.get('pk'))   
