# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-03 15:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('core', '0005_auto_20191003_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtraInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.CharField(max_length=512)),
                ('avatar', models.CharField(max_length=2048)),
            ],
        ),
    ]