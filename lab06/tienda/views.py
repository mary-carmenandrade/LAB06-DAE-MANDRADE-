from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria
# Create your views here.


# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    lista_categorias = Categoria.objects.all()
    print(product_list)
    print(lista_categorias)
    context = {
        'productos': product_list,
        'categorias' : lista_categorias
    }
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html', {'producto': producto})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    product_list = categoria.producto_set.all()
    lista_categorias = Categoria.objects.all()
    context = {
        'productos':product_list,
        'categorias':lista_categorias,
        'categoria':categoria
    }
    return render(request,'index.html',context)