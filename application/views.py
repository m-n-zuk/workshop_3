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

    # def post(self, request):
    #
    #     f_name = request.POST['f_name']
    #     l_name = request.POST['l_name']
    #
    #     Person.objects.create(first_name=f_name, last_name=l_name)
    #
    #     return redirect('/sklep/add_person')