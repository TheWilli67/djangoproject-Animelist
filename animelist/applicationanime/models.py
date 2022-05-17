from django.db import models

class Anime(models.Model):
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    annee_parution = models.CharField(max_length=50)
    nombre_episodes = models.IntegerField(blank=False)
    url_anime = models.CharField(max_length=150)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur} édité le {self.annee_parution}"
        return chaine
    
    def dictionnaire(self):
        return {"titre": self.titre, "auteur": self.auteur, "nombre_episodes": self.nombre_episodes,"url_anime": self.url_anime , "resume": self.resume}
    
############################################

class Site(models.Model):
    titre = models.CharField(max_length=100)
    tarif = models.CharField(max_length=10)
    url_site = models.CharField(max_length=150)

    def __str__(self):
        chaine = f"{self.titre} {self.tarif} son url : {self.url_site}"
        return chaine
    
    def dictionnairesite(self):
        return {"titre": self.titre,"tarif": self.tarif, "url":self.url_site}
    