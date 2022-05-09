from .form import AnimeForm, SiteForm, CommentaireForm
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
    return HttpResponseRedirect('/applicationanime/affichetout.html')

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
        form = SiteForm(request)
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
    return HttpResponseRedirect('/applicationanime/affichetoutsite/')

######################################################################################
######################################################################################
#Crud commentaire#####################################################################
######################################################################################

def affichagecommentaire(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    return render(request, 'applicationanime/affichagecommentaire.html', {"commentaire": commentaire})

def affichetoutcommentaire(request):
    listCommentaire = models.Commentaire.objects.all()
    return render(request, 'applicationanime/affichetoutcommentaire.html', {"listCommentaire": listCommentaire})

def traitementcommentaire(request):
    pForm = CommentaireForm(request.POST)
    if pForm.is_valid():
        commentaire = pForm.save()
        commentaire.save()
        return render(request, 'applicationanime/affichagecommentaire.html', {'commentaire': commentaire})
    else:
        return render(request, 'applicationanime/ajoutcommentaire.html', {'form': pForm})

def ajoutcommentaire(request):
    if request.method == "POST":
        form = CommentaireForm(request)
        if form.is_valid():
            commentaire = form.save()
            return render(request, "applicationanime/affichagecommentaire.html", {"commentaire": commentaire})
        else:
            return render(request, "applicationanime/ajoutcommentaire.html", {"form": form})
    else:
        form = CommentaireForm()
        return render(request, "applicationanime/ajoutcommentaire.html", {"form": form})
    
def updatecommentaire(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    form = CommentaireForm(site.dictionnairecommentaire())
    return render(request, "applicationanime/ajoutcommentaire.html", {"form": form, "id":id})

def updatetraitementcommentaire(request, id):
    pForm = CommentaireForm(request.POST)
    if pForm.is_valid():
        commentaire = pForm.save(commit=False)
        commentaire.id = id
        commentaire.save()
        return render(request, 'applicationanime/affichagecommentaire.html', {'commentaire': commentaire})
    else:
        return render(request, 'applicationanime/ajoutcommentaire.html', {'form': pForm})

def deletecommentaire(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    commentaire.delete()
    return HttpResponseRedirect('/applicationanime/affichetoutcommentaire/')