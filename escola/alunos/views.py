from django.shortcuts import render
from .models import Aluno

# Create your views here.
def cadastrar(request):
    if request.method == 'POST': 
        nome = request.POST['nome']
        matricula = request.POST['matricula']
        idade = request.POST['idade']
        email = request.POST['email']
        endereco = request.POST['endereco']
        tel = request.POST['tel']

        aluno = Aluno(nome = nome,matricula = matricula,idade = idade,email=email,endereco=endereco,tel=tel)
        aluno.save()

    return render(request, 'index.html')


def listar(request):    
    aluno = Aluno.objects.all()

    return render(request,'listar.html',{"alunos":aluno})

def pesquisar(request):
    if request.method == 'GET':
        nome = request.GET.get('nome', '')
        alunos = Aluno.objects.filter(nome__icontains = nome)
        return render(request,'pesquisar.html',{'alunos': alunos})