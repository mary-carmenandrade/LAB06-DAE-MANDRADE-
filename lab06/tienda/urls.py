from django.urls import path
from . import views
app_name = 'tienda'

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('producto/<int:producto_id>/', views.producto, name='producto')
]
