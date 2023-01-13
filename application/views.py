from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from application.models import *


# Create your views here.
class Test(View):

    def get(self, request):

        return HttpResponse("Witaj!")


class MainPage(View):

    def get(self, request):

        rooms = Room.objects.all()
        l_r = len(rooms)

        return render(request, 'main_page.html', {'rooms': rooms, 'l_r': l_r})



class AddRoom(View):

    def get(self, request):

        rooms = Room.objects.all()

        return render(request, 'add_room.html', {'rooms': rooms})

    def post(self, request):

        name = request.POST['name']
        capacity = request.POST['capacity']
        projector = request.POST.get('projector', False) == 'on'

        rooms_n = Room.objects.filter(name=name)

        if len(name) != 0:

            if len(rooms_n) == 0:

                if int(capacity) > 0:
                    Room.objects.create(name=name, capacity=capacity, projector=projector)
                    return redirect('/')
                else:
                    txt = "Conference room's capacity should be grater that 0!"
                    return render(request, 'add_room.html', {'txt': txt})

            else:
                txt = "A conference room with that name is existing! Write another name."
                return render(request, 'add_room.html', {'txt': txt})

        else:
            txt = "Conference room's name shouldn't be empty!"
            return render(request, 'add_room.html', {'txt': txt})


class RoomView(View):

    def get(self, request, id):

        room = Room.objects.get(id=id)

        return render(request, 'room.html', {'room': room})

