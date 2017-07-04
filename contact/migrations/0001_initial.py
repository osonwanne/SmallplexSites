# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Message', models.TextField(blank=True, verbose_name='Message')),
                ('Created', models.DateTimeField(auto_now=True, verbose_name='Created')),
            ],
        ),
    ]
