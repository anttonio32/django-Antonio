from django.shortcuts import render
from .models import Professor

# Create your views here.
def cadastrar(request):
    if request.method == 'POST': 
        nome = request.POST['nome']
        email = request.POST['email']
        tel = request.POST['tel']

        professor = Professor(nome = nome,email=email,tel=tel)
        professor.save()

    return render(request, 'professor.html')

def listar(request):
    professor = Professor.objects.all()

    return render(request,'listarProf.html',{'professor':professor})

def pesquisar(request): 
    if request.method == 'GET':
        nome = request.GET.get('nome', '')
        professor = Professor.objects.filter(nome__icontains = nome)
        return render(request, 'pesquisarProf.html',{'professor': professor})