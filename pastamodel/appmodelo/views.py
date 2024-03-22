# views.py

from django.shortcuts import render, redirect
from .forms import ClienteForm, ProdutoForm
from .models import Cliente, Produto

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})


def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

from django.http import HttpResponse



def pagina_inicial(request):
    return render(request, 'appmodelo/pagina_inicial.html')