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


def delete(request, myapp_id):
    Superheroes.objects.filter(id= myapp_id).delete()
    return HttpResponseRedirect(reverse('myapp:index'))


def edit(request, myapp_id):
    if request.method == 'POST':
        hero_edit = Superheroes.objects.get(id=myapp_id)
        hero_edit.name = request.POST.get('name')
        hero_edit.alter_ego = request.POST.get('alter_ego')
        hero_edit.primary_ability = request.POST.get('primary_ability')
        hero_edit.secondary_ability = request.POST.get('secondary_ability')
        hero_edit.catch_phrase = request.POST.get('catch_phrase')
        hero_edit.save()
        return HttpResponseRedirect(reverse('myapp:index'))
    else:
        hero_edit = Superheroes.objects.get(id=myapp_id)
        context = {
            'hero': hero_edit
        }
        return render(request, 'myapp/edit.html')


