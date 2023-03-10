import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from application.models import *


# Create your views here.
class Test(View):

    def get(self, request):

        return HttpResponse("Witaj!")


class MainPage(View):

    def get(self, request):

        rooms = Room.objects.order_by('name')

        return render(request, 'main_page.html', {'rooms': rooms, 'today': datetime.date.today()})


class AddRoom(View):

    def get(self, request):

        rooms = Room.objects.order_by('name')

        return render(request, 'add_room.html', {'rooms': rooms})

    def post(self, request):

        name = request.POST['name']
        capacity = request.POST['capacity']
        projector = request.POST.get('projector', False) == 'on'

        if len(name) != 0:

            if len(Room.objects.filter(name=name)) == 0:

                if int(capacity) > 0:
                    Room.objects.create(name=name, capacity=capacity, projector=projector)
                    return redirect('/')
                else:
                    txt = "Conference room's capacity should be integer grater that 0!"
                    return render(request, 'add_room.html', {'txt': txt})

            else:
                txt = "A conference room with that name is existing! Write another name."
                return render(request, 'add_room.html', {'txt': txt})

        else:
            txt = "Conference room's name shouldn't be empty!"
            return render(request, 'add_room.html', {'txt': txt})


class RoomDelete(View):

    def get(self, request, id):

        rooms = Room.objects.order_by('name')

        room = Room.objects.get(id=id)

        txt = f"Conference room: {room.name} has been deleted!"

        room.delete()

        return render(request, 'main_page.html', {'rooms': rooms, 'txt': txt})


class ModifyRoom(View):

    def get(self, request, id):

        room = Room.objects.get(id=id)

        return render(request, 'modify_room.html', {'room': room})

    def post(self, request, id):

        rooms = Room.objects.order_by('name')

        room = Room.objects.get(id=id)
        txt = f"Conference room: {room.name} has been modified!"
        name = request.POST['name']
        capacity = request.POST['capacity']
        projector = request.POST.get('projector', False) == 'on'

        if len(name) != 0:

            if (len(Room.objects.filter(name=name)) == 1 and name == room.name) or len(Room.objects.filter(name=name)) == 0:

                if int(capacity) > 0:
                    room.name = name
                    room.capacity = capacity
                    room.projector = projector
                    room.save()

                    return render(request, 'main_page.html', {'rooms': rooms, 'txt': txt})

                else:
                    txt = "Conference room's capacity should be integer grater that 0!"
                    return render(request, 'add_room.html', {'txt': txt})

            else:
                txt = "A conference room with that name is existing! Write another name."
                return render(request, 'add_room.html', {'txt': txt})

        else:
            txt = "Conference room's name shouldn't be empty!"
            return render(request, 'add_room.html', {'txt': txt})


class RoomReservation(View):

    def get(self, request, id):

        room = Room.objects.get(id=id)

        return render(request, 'room_reservation.html', {'room': room})

    def post(self, request, id):

        date = request.POST['date']
        comment = request.POST['comment']
        room = Room.objects.get(id=id)

        if date < str(datetime.date.today()):
            return render(request, 'room_reservation.html', {'txt': "The date is past!"})

        if Reservation.objects.filter(date=date, room_id=id):
            return render(request, 'room_reservation.html', {'txt': "The room is reserved already!"})

        Reservation.objects.create(room_id=room, date=date, comment=comment)

        return redirect('/')


class RoomView(View):

    def get(self, request, id):

        room = Room.objects.get(id=id)
        reservation = Reservation.objects.filter(room_id=room, date__gte=datetime.date.today()).order_by('date')

        return render(request, 'room.html', {'room': room, 'res': reservation})


