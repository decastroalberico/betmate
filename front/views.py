from django.shortcuts import render
from front.models import Eventos

def index(request):
    eventos = Eventos.objects.all()
    return render(request, 'index.html', {"cards":eventos})
def detalhes(request):
    return render(request, 'detalhes.html')
def eventos(request):
    return render(request, 'eventos.html')