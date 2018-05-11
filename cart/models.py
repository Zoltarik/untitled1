from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class tblCategory(models.Model):
    nameCategory = models.CharField(max_length=100)


class tblPublesher(models.Model):
    namePublesher = models.CharField(max_length=100)


class tblBook(models.Model):
    nameBook = models.TextField()
    fioAuthor = models.CharField(max_length=100)
    countPage = models.IntegerField()
    bookPrice = models.IntegerField()
    linkImage = models.ImageField(upload_to='img/', blank=True, verbose_name='Обложка')
    countBookWarhouse = models.IntegerField()
    publesher = models.ForeignKey(tblPublesher, on_delete=models.CASCADE)
    category = models.ForeignKey(tblCategory, on_delete=models.CASCADE)


class tblCart(models.Model):
    book = models.ForeignKey(tblBook, on_delete=models.CASCADE)
    cartUser = models.ForeignKey(User, on_delete=models.CASCADE)
    countBook = models.IntegerField()
    send = models.BooleanField()
    close = models.BooleanField()