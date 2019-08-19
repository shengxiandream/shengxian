# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from datetime import datetime
from django.db import models


class User(models.Model):
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=2, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    regtime = models.DateTimeField(default=datetime.now)
    lasttime = models.DateTimeField(blank=True, null=True)
    login_type = models.CharField(max_length=2,default=1)
    tx = models.CharField(max_length=256, blank=True, null=True)
    rname = models.CharField(max_length=20, null=True, default='')

    class Meta:
        managed = True
        db_table = 'User'


class Auser(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=128)
    type = models.IntegerField(default=1)
    regtime = models.DateTimeField(default=datetime.now)
    tx = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'auser'

    # 商品分类
class Type(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.IntegerField()
    def __str__(self):
        return self.ttitle
    class Meta:
        managed = True
        db_table = 'type'

# 商品
class Good(models.Model):
    name = models.CharField(max_length=20)
    titleid = models.IntegerField()
    # 图片位置
    pic = models.CharField(max_length=100)
    # 零售价
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # 成本
    costing = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.IntegerField(default=1)  # 1商品上架，0下架商品
    # 点击量  用于排序
    click = models.IntegerField(default=0)
    # 库存
    kucun = models.IntegerField()
    # 详细介绍
    content = models.CharField(max_length=200)
    xq = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'good'



class Aplate(models.Model):
    name = models.CharField(max_length=50)
    aid = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'aplate'

#购物车
class Order(models.Model):
    uid = models.IntegerField()
    gid = models.IntegerField()
    # 订单时间
    time = models.DateField(default=datetime.now)
    # 数量
    quantity = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'order'



# 订单
class indent(models.Model):
    uid = models.IntegerField()   #用户
    gid = models.IntegerField()   #商品
    oid = models.IntegerField()   #订单
    payable = models.DecimalField(max_digits=5,decimal_places=2)  #应付金额
    paid = models.DecimalField(max_digits=5,decimal_places=2)     #已付金额
    consignee = models.CharField(max_length=30)  #收件人
    pay = models.IntegerField(default=0)   #是否支付  0否  1是  2到付
    type = models.IntegerField(default=0)   #是否退换货 0正常 1已退 2处理中 3客户作废  4系统作废
    express = models.IntegerField(default=0)  #是否发货  0未发货  1代发货 2配送中  3已送达(未签收)  4交易完成
    class Meta:
        managed = True
        db_table = 'indent'


#收货地址
class shipping(models.Model):
    uid = models.IntegerField()
    username = models.CharField(max_length=20)
    #地址
    site = models.CharField(max_length=200)
    youbian = models.CharField(max_length=6,default='')
    phone = models.CharField(max_length=11)
    class Meta:
        managed = True
        db_table = 'city'





