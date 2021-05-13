from products.models import Product
from comments.models import Comment
from comments.forms import CommentForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def views_create(request, product):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Method 1
            # form.save()

            # Method 2
            # comment = Comment(name=request.POST['name'], comment=request.POST['comment'], product=product)
            # comment.save()

            # Method 3
            product = Product.objects.get(pk=product)
            product.comments.create(name=request.POST['name'], comment=request.POST['comment'])

            return redirect('products:product_show', product.id)

    return HttpResponse({ 'message': 'works '})