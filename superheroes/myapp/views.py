from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superheroes
from django.urls import reverse
# Create your views here.


def index(request):
    all_superheroes = Superheroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'myapp/index.html', context)


def detail(request, myapp_id):
    result = Superheroes.objects.get(id=myapp_id)
    context = {
        'result': result
    }
    return render(request, 'myapp/details.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superheroes(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catch_phrase=catch_phrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('myapp:index'))
    else:
        return render(request, 'myapp/create.html')
