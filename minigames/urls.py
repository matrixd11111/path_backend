from django.urls import path
from .views import *

app_name = 'minigames'

urlpatterns = [
    path('', MiniGamesView.as_view()),
    path('loto/<int:menu>/', LotoGameView.as_view(), name='loto'),
    path('loto/<int:ticket>/<int:number>/', LotoGameView.as_view(), name='loto'),
]
