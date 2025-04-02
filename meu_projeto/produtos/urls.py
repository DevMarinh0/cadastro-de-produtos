from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
]
