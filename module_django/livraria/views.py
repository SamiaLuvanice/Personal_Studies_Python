from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, esta é a página inicial.")

def sobre(request):
    return HttpResponse("Olá, esta é a página sobre.")