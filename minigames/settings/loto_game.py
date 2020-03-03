import random
import json

from ..models import *

# создание класса билета
class Ticket():

    def show_ticket(self, number_ticket, tickets):
        ticket = json.loads(tickets.replace("\'", "\""))
        return ticket[(f'{number_ticket}')]
        

    def _save_models(self, ticket, number_tickets, user_name=None):

        user = UserIdModel.objects.get(user=user_name)
        if user_name == user.user:
            user_ticket = LotoGameModel.objects.filter(
                user=user
            ).values('ticket')

            if not user_ticket:
                user = UserIdModel.objects.get(user=user_name)
                new_ticket = {(f'{number_tickets}'): (f'{ticket}')}
                ticket = LotoGameModel.objects.create(user=user, ticket=new_ticket)
                ticket.save()
            else:
                strTicket = user_ticket.first().get('ticket').replace("\'", "\"")
                tickets = json.loads(strTicket)
                if str(number_tickets) not in tickets.keys():
                    tickets[(f'{number_tickets}')] = (f'{ticket}')
                user_ticket.update(ticket=tickets)

    def create_ticket(self, user_name, number_tickets, update=False,):
        ticket = []

        for x in range(3):
            line_ticket = [0 for i in range(9)]
            while line_ticket.count(0) != 4:
                choice_number = random.choice(range(1, 100))
                choice_index = random.choice(range(0, 8))
                if not ticket.count(choice_number):
                    line_ticket[choice_index] = choice_number
            ticket.append(line_ticket)
        if update:
            self._save_models(ticket, number_tickets, user_name=user_name,)

    def cross_it_uot(self, ticket, number):

        if len(self.ticket_list) >= 1:
            tickets = self.ticket_list[ticket]
            for i in tickets:
                if number in i:
                    a, b = tickets.index(i), i.index(number)
                    self.ticket_list[ticket][a][b] = 0

    """Метод принимает на вход число проверяет есть ли оно в билете
    если ДА вычеркивает, так же проверяет остались ли еще числа не равные
    0 в билете
    переменные a,b временно для PEP"""

    def check_ticket(self, check_num=None):

        if check_num:
            if len(self.ticket_list) >= 1:
                for i in self.ticket_list:
                    for j in i:
                        if check_num in j:
                            a, b = self.ticket_list.index(i), i.index(j)
                            self.ticket_list[a][b][j.index(check_num)] = 111

    """Удалить билет"""

    def delete_ticket(self):
        pass

# создание класса мешка с боченками
class BarrelBag():

    def __init__(self):
        self.barrel_list = []
        self.barrel_pop = []
        self.barrel_other = 111

    """Создание мешка с бочонками"""

    def create_barrel(self):
        for i in range(1, 100):
            self.barrel_list.append(i)

        """возврат рандомно выбранного боченкa
        это под вопросом?"""

    def get_barrel(self):
        barrel = random.choice(self.barrel_list)
        index_barrel = self.barrel_list.index(barrel)
        if len(self.barrel_pop) == 5:
            self.barrel_other = self.barrel_pop[0]
            self.barrel_pop.remove(self.barrel_pop[0])

        self.barrel_pop.append(self.barrel_list.pop(index_barrel))

    """Метод удаляет бочонок из мешка"""

    def del_barrel(self, barrel):
        self.barrel_list.remove(barrel)




class Game():

    def __init__(self):
        pass


if __name__ == '__main__':
    pass
