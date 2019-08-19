# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-07-10 12:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20190706_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='indent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('gid', models.IntegerField()),
                ('oid', models.IntegerField()),
                ('payable', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('consignee', models.CharField(max_length=30)),
                ('pay', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('express', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
                'db_table': 'indent',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('gid', models.IntegerField()),
                ('time', models.DateField(default=datetime.datetime.now)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'managed': True,
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
                ('site', models.CharField(max_length=200)),
                ('youbian', models.CharField(default='', max_length=6)),
                ('phone', models.CharField(max_length=11)),
            ],
            options={
                'managed': True,
                'db_table': 'city',
            },
        ),
    ]
