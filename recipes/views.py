from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz Otavio',
    })


def contato(request):
    return HttpResponse('contato 2')


def sobre(request):
    return HttpResponse('sobre')
