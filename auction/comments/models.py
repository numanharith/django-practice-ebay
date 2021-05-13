from django.db.models.fields import related
from products.models import Product
from django.db import models
import uuid

# Create your models here.
class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=200, null=False)
    comment = models.TextField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')