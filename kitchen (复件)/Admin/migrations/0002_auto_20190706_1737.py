# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-06 09:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('aid', models.IntegerField()),
            ],
            options={
                'db_table': 'aplate',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Auser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=128)),
                ('type', models.IntegerField(default=1)),
                ('regtime', models.DateTimeField(default=datetime.datetime.now)),
                ('tx', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'auser',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('titleid', models.IntegerField()),
                ('pic', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('costing', models.DecimalField(decimal_places=2, max_digits=5)),
                ('isDelete', models.IntegerField(default=1)),
                ('click', models.IntegerField()),
                ('kucun', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'good',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GoodT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Good')),
            ],
            options={
                'db_table': 'goodt',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('titleid', models.IntegerField()),
            ],
            options={
                'db_table': 'type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('sex', models.CharField(blank=True, max_length=2, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('regtime', models.DateTimeField(default=datetime.datetime.now)),
                ('lasttime', models.DateTimeField(blank=True, null=True)),
                ('login_type', models.CharField(default=1, max_length=2)),
                ('tx', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='goodt',
            name='typelist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Type'),
        ),
    ]
