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
            return redirect('listar_pedido')  # Supondo que haja uma view para listar os pedidos
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
def alterar_pedido(request, pedido_id):
    # Lógica para obter o pedido e renderizar o formulário de alteração
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        # Lógica para processar o formulário de alteração
        # Redirecionar para a página de detalhes do pedido após a alteração
        return redirect('detalhes_pedido', pedido_id=pedido.id)
    else:
        # Renderizar o formulário de alteração com os dados do pedido
        return render(request, 'alterar_pedido.html', {'pedido': pedido})
def deletar_pedido(request, pedido_id):
    # Lógica para deletar o pedido
    pedido = Pedido.objects.get(id=pedido_id)
    pedido.delete()
    # Redirecionar para a página de listar pedidos após a exclusão
    return redirect('listar_pedidos')

# Views para alterar e deletar cliente e produto
def alterar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        # Lógica para processar o formulário de alteração do cliente
        return redirect('listar_clientes')
    else:
        return render(request, 'alterar_cliente.html', {'cliente': cliente})

def deletar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')

def alterar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        # Lógica para processar o formulário de alteração do produto
        return redirect('listar_produtos')
    else:
        return render(request, 'alterar_produto.html', {'produto': produto})

def deletar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect('listar_produtos')