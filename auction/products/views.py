from products.models import Product
from django.shortcuts import render, redirect
from products.forms import ProductForm
from django.contrib import messages

# Create your views here.
def views_index(request):
    form = ProductForm()

    # POST request
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product has been added.")
            return redirect('products_index')
        else:
            messages.error(request, "Error: Product failed to add.")
            return redirect('products_index')

    # GET request
    products = Product.objects.all()

    return render(request, 'products/index.html', { "form": form, "products": products })

def views_show(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return redirect('products_index')
        
    form = ProductForm(instance=product)
             
    # if user SUBMITS EDIT FORM
    if request.GET.get('action') == 'edit' and request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_show', product.id)

    # if user CLICKS EDIT
    if request.GET.get('action') == 'edit':
        return render(request, 'products/show.html', { "form": form, "product": product, "edit": True })

    # if user CLICKS DELETE
    if request.GET.get('action') == 'del':
        product.delete()
        return redirect('products_index')

    return render(request, 'products/show.html', { "form": form, "product": product, "edit": False })