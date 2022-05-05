from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AnimeForm(ModelForm):
    class Meta:
        model = models.Anime
        fields = ('titre', 'auteur', 'annee_parution', 'nombre_episodes','url_anime','resume')
        labels = {
        'titre' : _('Titre'),
        'auteur' : _('Auteur') ,
        'annee_parution' : _('date de parution'),
        'nombre_pages' : _('nombres de pages'),
        'url_anime' : _('url de l"anime'),
        'resume' : _('Résumé'),
    }
