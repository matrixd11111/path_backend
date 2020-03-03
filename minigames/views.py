from django.shortcuts import render, HttpResponseRedirect
from rest_framework.generics import ListAPIView, ListCreateAPIView

from .models import *
from .serializer import *
from .settings import loto_game
import asyncio

class MiniGamesView(ListAPIView):
    serializer_class = UserIdSerializer
    
    def get_queryset(self):
        user = self.request.user.username
        queryset = UserIdModel.objects.filter(user__contains=user)
        if user:
            if not queryset:
                UserIdModel.objects.create(user=user)

            if user != queryset.first().user:
                UserIdModel.objects.create(user=user)

        return queryset
        

class LotoGameView(ListAPIView):
    serializer_class = LotoGameSerializer

    def get_queryset(self):
        user = self.request.user.username

        if not user:
            user = 'Anonimus'

        user_id = UserIdModel.objects.filter(user__contains=user).first().id
        queryset = LotoGameModel.objects.filter(user=user_id)
        menu = self.kwargs.get('menu')
        number_ticket = self.kwargs.get('ticket')
        number_change = self.kwargs.get('number')
        print(dir(asyncio))
        
        if menu == 1:
            pass

        if menu == 2:
            if not queryset:
                ticket = loto_game.Ticket()
                ticket.create_ticket(user, create=True)

        if number_ticket:
            i = queryset.values_list('ticket')
#            i = LotoGameModel.objects.filter(ticket="{'1': '[[35, 46, 0, 51, 0, 17, 7, 0, 0], [47, 0, 13, 0, 60, 78, 0, 95, 0], [0, 0, 53, 99, 54, 0, 79, 84, 0]]', '2': '[[0, 73, 51, 0, 0, 40, 55, 31, 0], [45, 0, 0, 93, 50, 73, 25, 0, 0], [0, 0, 25, 0, 34, 79, 42, 37, 0]]', '3': '[[1, 0, 16, 0, 32, 61, 0, 99, 0], [92, 25, 0, 60, 18, 54, 0, 0, 0], [49, 85, 74, 0, 0, 0, 16, 38, 0]]'}")
#            print(i)
            #show_ticket = queryset.values('ticket').first().get('ticket')
            ticket = loto_game.Ticket()
            ticket.create_ticket(user, 
                                 update=True, 
                                 number_tickets=number_ticket,
            )
            

        return queryset

"""
class GameMenuViews(RedirectView):

    pattern_name = 'minigames/loto/lotogame.html'

    def get_redirect_url(self, *args, **kwargs):

        if kwargs.get('menu') == 1:
            ticket.create_ticket()

        if kwargs.get('menu') == 2:
            if len(barrel.barrel_list) == 0:
                barrel.create_barrel()
            else:
                print('Delete barrel')

        if kwargs.get('menu') == 3:
            barrel.barrel_list.clear()
            ticket.ticket_list.clear()

# данное условие временно. Эту ссылку необходимо
# переделать на автоматичесскую в javascript

        if kwargs.get('menu') == 15:
            barrel.get_barrel()

        return super().get_redirect_url(*args, **kwargs)


class ChengeTicketViews(RedirectView):

    pattern_name = 'minigames/loto/lotogame.html'

    def get_redirect_url(self, *args, **kwargs):

        if kwargs.get('pk') in barrel.barrel_pop:
            ticket.cross_it_uot((kwargs.get('ticket')-1),
                                kwargs.get('pk'),)

        return super().get_redirect_url(*args, **kwargs)


def test(request):
    ticket.check_ticket(check_num=barrel.barrel_other)
    barrel.get_barrel()
    return HttpResponseRedirect('/minigame/lotogame')
"""
