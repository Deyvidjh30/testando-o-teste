from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('feed/', views.feed_view, name='feed'),
    path('admin-painel/', views.admin_panel_view, name='admin_panel'),
]
