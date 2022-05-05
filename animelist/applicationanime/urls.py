from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('index/', views.index),
    path('main/', views.main),
    path('affichetout/', views.affichetout),
    path('traitement/', views.traitement),
    path('ajout/', views.ajout),
    path('affichage/<int:id>/',views.affichage),
    path('update/<int:id>/',views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
]
