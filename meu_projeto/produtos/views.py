from django.shortcuts import render, redirect
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        preco = request.POST['preco']
        Produto.objects.create(nome=nome, preco=preco)
        return redirect('listar_produtos')
    return render(request, 'produtos/cadastrar.html')
