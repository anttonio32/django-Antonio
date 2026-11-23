from django.urls import path
from . import views

urlpatterns = [
    path('cadastrarProfessor/',views.cadastrar,name='cadastrarProfessor/'),
    path('listarProfessor/',views.listar,name='listarProfessor/'),
    path('pesquisarProfessor/',views.pesquisar,name='pesquisarProfessor/'),
]