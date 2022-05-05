from .form import AnimeForm, SiteForm
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
        anime.save()
        return render(request, 'applicationanime/affichage.html', {'anime': anime})
    else:
        return render(request, 'applicationanime/ajout.html', {'form': pForm})


def affichage(request, id):
    anime = models.Anime.objects.get(pk=id)
    return render(request, 'applicationanime/affichage.html', {"anime": anime})


def affichetout(request):
    listAnim = models.Anime.objects.all()
    return render(request, 'applicationanime/affichetout.html', {"listAnim": listAnim})


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
    return HttpResponseRedirect('/applicationanime/index/')

#############CRUD n°2######################################CRUD n°2#######################
#########################CRUD n°2##############CRUD n°2###################################
#CRUD n°2#################################################################################
################################################################CRUD n°2#################

def affichagesite(request, id):
    site = models.Site.objects.get(pk=id)
    return render(request, 'applicationanime/affichagesite.html', {"site": site})

def affichetoutsite(request):
    listSite = models.Site.objects.all()
    return render(request, 'applicationanime/affichetoutsite.html', {"listSite": listSite})

def traitementsite(request):
    pForm = SiteForm(request.POST)
    if pForm.is_valid():
        site = pForm.save()
        site.save()
        return render(request, 'applicationanime/affichagesite.html', {'site': site})
    else:
        return render(request, 'applicationanime/ajoutsite.html', {'form': pForm})

def ajoutsite(request):
    if request.method == "POST":
        form = AnimeForm(request)
        if form.is_valid():
            site = form.save()
            return render(request, "applicationanime/affichagesite.html", {"site": site})
        else:
            return render(request, "applicationanime/ajoutsite.html", {"form": form})
    else:
        form = SiteForm()
        return render(request, "applicationanime/ajoutsite.html", {"form": form})
    
def updatesite(request, id):
    site = models.Site.objects.get(pk=id)
    form = SiteForm(site.dictionnairesite())
    return render(request, "applicationanime/ajoutsite.html", {"form": form, "id":id})

def updatetraitementsite(request, id):
    pForm = SiteForm(request.POST)
    if pForm.is_valid():
        site = pForm.save(commit=False)
        site.id = id
        site.save()
        return render(request, 'applicationanime/affichagesite.html', {'site': site})
    else:
        return render(request, 'applicationanime/ajoutsite.html', {'form': pForm})

def deletesite(request, id):
    site = models.Site.objects.get(pk=id)
    site.delete()
    return HttpResponseRedirect('/applicationanime/index/')