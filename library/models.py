from django.db import models


class book(models.Model):
    name = models.CharField(max_length=200)
    book_cat = models.CharField(max_length=100)
    page = models.IntegerField()
    price = models.IntegerField()


