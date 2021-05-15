from comments.forms import CommentForm
from products.models import Product
from django.shortcuts import render, redirect
from products.forms import *
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
            return redirect('products:products_index')
        else:
            messages.error(request, "Error: Product failed to add.")
            return redirect('products:products_index')

    # GET request
    products = Product.objects.all()

    return render(request, 'products/index.html', { "form": form, "products": products })

def view_show(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return redirect('products:products_index')
        
    form = ProductForm(instance=product)
             
    # if user SUBMITS EDIT FORM; when url has ?action=edit and is a POST request
    if request.GET.get('action') == 'edit' and request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_show', product.id)

    # if user CLICKS EDIT; when url has ?action=edit and is a GET request
    if request.GET.get('action') == 'edit':
        return render(request, 'products/show.html', { "form": form, "product": product, "edit": True })

    # if user CLICKS DELETE; when url has ?action=del and is a GET request
    if request.GET.get('action') == 'del':
        product.delete()
        return redirect('products:products_index')

    comment_form = CommentForm()
    context = { "form": form, "product": product, "edit": False, "comment_form": comment_form }
    return render(request, 'products/show.html', context)

def view_create_category(request):
    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('products:products_index')

    context = { "category_form": category_form }
    return render(request, 'products/create_category.html', context)