from django.db import models


# Create your models here.

class Product(models.Model):
    db_table = 'products'
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    db_table = 'ratings'
    star = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

