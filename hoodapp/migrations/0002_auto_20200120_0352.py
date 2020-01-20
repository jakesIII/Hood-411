# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-20 03:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hood',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hood', to=settings.AUTH_USER_MODEL),
        ),
    ]