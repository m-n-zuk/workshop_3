from django.shortcuts import render, redirect, HttpResponse
from django.views import View



# Create your views here.
class Test(View):

    def get(self, request):

        return HttpResponse("Witaj!")

