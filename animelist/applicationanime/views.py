from .form import AnimeForm
from django.utils.translation import gettext_lazy as _
from . import models
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'applicationanime/index.html')

def main(request):
    return render(request, 'main.html')

def traitement(request):
    pForm = AnimeForm(request.POST)
    if pForm.is_valid():
        anime = pForm.save()
        return render(request, 'applicationanime/affichage.html', {'anime': anime})
    else:
        return render(request, 'applicationanime/ajout.html', {'form': pForm})


def affichage(request, id):
    anime = models.Anime.objects.get(pk=id)
    return render(request, 'applicationanime/affichage.html', {"anime": anime})


def affichetout(request):
    anime = models.Anime.objects.all()
    return render(request, 'applicationanime/affichetout.html', {"anime": anime})


def ajout(request):
    if request.method == "POST":
        form = AnimeForm(request)
        if form.is_valid():
            anime = form.save()
            return render(request, "applicationanime/affichage.html", {"anime": anime})
        else:
            return render(request, "applicationanime/ajout.html", {"form": form})
    else:
        form = AnimeForm()
        return render(request, "applicationanime/ajout.html", {"form": form})



def update(request, id):
    anime = models.Anime.objects.get(pk=id)
    form = AnimeForm(anime.dictionnaire())
    return render(request, "applicationanime/ajout.html", {"form": form, "id":id})

def updatetraitement(request, id):
    pForm = AnimeForm(request.POST)
    if pForm.is_valid():
        anime = pForm.save(commit=False)
        anime.id = id
        anime.save()
        return render(request, 'applicationanime/affichage.html', {'anime': anime})
    else:
        return render(request, 'applicationanime/ajout.html', {'form': pForm})

def delete(request, id):
    anime = models.Anime.objects.get(pk=id)
    anime.delete()
    return HttpResponseRedirect('/applicationanime/')