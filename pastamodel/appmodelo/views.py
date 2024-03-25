# views.py

from django.shortcuts import render, redirect
from .forms import ClienteForm, ProdutoForm, PedidoForm
from .models import Cliente, Produto, Pedido
from django.http import HttpResponse
from django.shortcuts import render, redirect

def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedido')  # Supondo que haja uma view para listar os pedidos
    else:
        form = PedidoForm()
    return render(request, 'cadastrar_pedido.html', {'form': form})



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

def pagina_inicial(request):
    return render(request, 'appmodelo/pagina_inicial.html')

def listar_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listar_pedido.html', {'pedidos': pedidos})