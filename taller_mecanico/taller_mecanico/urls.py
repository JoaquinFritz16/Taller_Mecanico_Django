from django.contrib import admin
from django.urls import path
from taller import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),
    path('login/', views.login_empleados, name='login'),
]
