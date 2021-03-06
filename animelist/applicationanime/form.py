from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AnimeForm(ModelForm):
    class Meta:
        model = models.Anime
        fields = ('titre', 'auteur', 'annee_parution', 'nombre_episodes','url_anime','resume')
        labels = {
        'titre' : _('Titre'),
        'auteur' : _('Éditeur') ,
        'annee_parution' : _('date de parution'),
        'nombre_pages' : _('nombres de pages'),
        'url_anime' : _('url de l anime'),
        'resume' : _('Résumé'),
    }

class SiteForm(ModelForm):
    class Meta:
        model = models.Site
        fields = ('titre','tarif','url_site', )
        labels = {
        'titre' : _('Titre'),
        'tarif' : _('Tarif annuel'),
        'url_anime' : _('url de l anime'),
    }