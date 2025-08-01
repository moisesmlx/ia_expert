from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cifra', views.cifra, name='cifra'),
    path('cifra_unidade', views.cifra_unidade, name='cifra_unidade'),
    path('info', views.info, name='info'),
    path('download', views.download, name='download')
]
