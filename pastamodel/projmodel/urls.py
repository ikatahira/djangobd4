from django.contrib import admin
from django.urls import path, include
from appmodelo import views  # Importe as views do aplicativo appmodelo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial'),  # Página inicial
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),  # Rota para cadastrar cliente
    path('clientes/', views.listar_clientes, name='listar_clientes'),  # Rota para listar clientes
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),  # Rota para cadastrar produto
    path('produtos/', views.listar_produtos, name='listar_produtos'),  # Rota para listar produtos
    path('pedidos/cadastrar/', views.cadastrar_pedido, name='cadastrar_pedido'),
    path('pedidos', views.listar_pedido, name='listar_pedido'),


]
