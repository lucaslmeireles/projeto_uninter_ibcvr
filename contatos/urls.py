from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.PagInicial.as_view(), name='index'),
]
