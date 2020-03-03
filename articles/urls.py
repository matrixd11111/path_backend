from django.urls import path

from .views import *

urlpatterns = [
    path('', SectionListView.as_view()),
    path('<int:pk>/', ThemeListView.as_view()),
    path('pablic/<int:pk>/', PablicationView.as_view()),
    
]
