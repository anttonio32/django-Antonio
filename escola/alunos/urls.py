from django.urls import path
from . import views

urlpatterns = [
    path('',views.cadastrar,name='cadastrarAluno/'),
    path('listarAluno/',views.listar,name='listarAluno/'),
    path('pesquisarAluno/',views.pesquisar,name='pesquisarAluno/'),
]