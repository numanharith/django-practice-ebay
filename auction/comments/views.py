import json
from django.contrib.auth.decorators import login_required
from products.models import Product
from comments.models import Comment
from comments.forms import CommentForm
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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
            product.comments.create(name=request.user.username, comment=request.POST['comment'])

            return redirect('products:product_show', product.id)

    return HttpResponse({ 'message': 'works '})

@csrf_exempt 
@login_required
def view_comments(request, product_id):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode(encoding='UTF-8'))
        # Find instance of product
        product = Product.objects.get(pk=product_id)
        # Use instance of product to save comments
        product.comments.create(
            name=json_data['name'],
            comment=json_data['comment'],
            product=product_id
        )
        return JsonResponse({'message': 'success'}, status=200, safe=True)
    
    comments = Comment.objects.filter(product=product_id)
    serialize = [c.serialize() for c in comments]
    return JsonResponse(serialize, safe=False)