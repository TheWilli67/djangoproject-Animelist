from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main/', views.main),
    path('affichetout/', views.affichetout),
    path('traitement/', views.traitement),
    path('ajout/', views.ajout),
    path('affichage/<int:id>/',views.affichage),
    path('update/<int:id>/',views.update),
    path('affichetout/', views.affichetout),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
    path('affichetoutsite/', views.affichetoutsite),
    path('ajoutsite/', views.ajoutsite),
    path('updatesite/<int:id>/',views.updatesite),
    path('deletesite/<int:id>/', views.deletesite),
    path('traitementsite/', views.traitementsite),
    path('affichagesite/<int:id>/',views.affichagesite),
    path('updatetraitementsite/<int:id>/', views.updatetraitementsite),
    path('updatecommentaire/<int:id>/', views.updatecommentaire),
    path('affichagecommentaire/<int:id>/', views.affichagecommentaire),
    path('ajoutcommentaire/', views.ajoutcommentaire),
    path('affichetoutcommentaire/', views.affichetoutcommentaire),
    path('traitementcommentaire/', views.traitementcommentaire),
]
