from products.models import Product
from django.test import TestCase

# Create your tests here.
class ProductTest(TestCase):
    def setUp(self):
        self.product = Product(
            name="White batik shirt",
            description="White in colour.",
            imgurl="https://dynamic.zacdn.com/k2cMiZFGyIs7Z46J23iSBtlFseo=/fit-in/346x500/filters:quality(95):fill(ffffff)/http://static.sg.zalora.net/p/gene-martino-1947-815789-1.jpg",
            price=50.00,
        )
        self.product.save()

    def test_product_exist(self):
        self.assertEqual(f'{self.product.name}', "White batik shirt")
        self.assertEqual(f'{self.product.description}', "White in colour.")

    def test_product_show(self):
        response = self.client.get('/show/33214-4323')
        self.assertEqual(response.status_code, 404)

    def test_book_show_pass_test(self):
        response = self.client.get(self.product.get_absolute_url())
        self.assertEqual(response.status_code, 200)