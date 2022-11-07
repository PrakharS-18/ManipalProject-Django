from django.db import models
from .product import Product

# making database dynamic for products

class SubProduct(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/')
    description = models.CharField(max_length=500,default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    # @staticmethod
    # def get_all_subproducts():
    #     return SubProduct.objects.all()

    @staticmethod
    def get_by_productid(product_id):
        if product_id:
            return SubProduct.objects.filter(product = product_id)
        else:
            return SubProduct.objects.all()

    # @staticmethod
    # def get_description_by_subproduct_id(subproduct_id):
    #     if subproduct_id:
    #         return SubProduct.objects.filter(subproduct = subproduct_id)
    #     else:
    #         return SubProduct.objects.all()


