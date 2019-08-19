from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

from django.db.models import Model


class Book(models.Model):
    bookname = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=200)
    year = models.DateField()
    pages = models.IntegerField(max_length=50)
    price = models.FloatField(max_length=50)
    pack = models.CharField(max_length=50)
    ISBN = models.FloatField(max_length=100)
    jj = models.CharField(max_length=1000)
    tt = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.
    class Meta:
        db_table = 'Book'

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sendnumber = models.IntegerField(max_length=50,blank=True,default=0)
    obtainnumber = models.IntegerField(max_length=50,blank=True,default=0)
    fishbean = models.CharField(max_length=50,blank=True,default=0)
    usertype = models.IntegerField(max_length=10,blank=True,default=0)

    class Meta:
        db_table = 'User'

class Transaction(models.Model):
    qiuid = models.IntegerField(max_length=50)
    shouusername = models.CharField(max_length=50)
    shoulocation = models.CharField(max_length=500)
    liuyan = models.CharField(max_length=1000,blank=True)
    phone = models.IntegerField(max_length=50)
    ISBN = models.FloatField(max_length=50)
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    tt = models.CharField(max_length=100)
    songid = models.IntegerField(max_length=50)
    listid = models.IntegerField(max_length=50)
    songusername = models.CharField(max_length=100)
    status = models.IntegerField(max_length=10,default=0)
    datatime = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'Transaction'

class Sendlist(models.Model):
    uid = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='gift_user', null=True)
    bookid = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='gift_book', null=True)
    # username = models.CharField(max_length=100)
    # bookname = models.CharField(max_length=100)
    send = models.IntegerField(max_length=10,blank=True,default=0)
    sendtime = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'Sendlist'

class Wishlist(models.Model):
    uid = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='wish_id',null=True)
    bookid=models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='wish_book',null=True)
    # username = models.CharField(max_length=100)
    # bookname = models.CharField(max_length=100)
    wish = models.IntegerField(max_length=10,blank=True,default=0)
    wishtime = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'Wishlist'
