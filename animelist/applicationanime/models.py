from django.db import models

class Anime(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    annee_parution = models.CharField(max_length=100)
    nombre_episodes = models.IntegerField(blank=False)
    url_anime = models.CharField(max_length=100)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur} édité le {self.annee_parution}"
        return chaine
    
    def dictionnaire(self):
        return {"titre": self.titre, "auteur": self.auteur, "nombre_episodes": self.nombre_episodes,"url_anime": self.url_anime , "resume": self.resume}
    
############################################

class Site(models.Model):
    titre = models.CharField(max_length=100)
    url_site = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.titre} et son url : {self.url_site}"
        return chaine
    
    def dictionnairesite(self):
        return {"titre": self.titre, "url":self.url_site}

###############################################


class Commentaire(models.Model):
    pseudo = models.CharField(max_length=20)
    text = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.pseudo} et son url : {self.text}"
        return chaine
    
    def dictionnairecommentaire(self):
        return {"pseudo": self.pseudo, "text":self.text}