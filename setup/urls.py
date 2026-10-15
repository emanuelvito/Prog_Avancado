from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('ramais/', views.consulta_ramais_view, name='ramais'),  
    path('ti/', views.login_view, name='login_ti'),  # Apontando para a view de login/autenticação
    path('painel/', views.painel_ti_view, name='painel_ti'),
]