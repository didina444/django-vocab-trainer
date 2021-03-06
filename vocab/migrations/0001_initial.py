# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 21:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Learnset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learnset_name', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('translation', models.CharField(max_length=200)),
                ('forms', models.CharField(default='', max_length=200)),
                ('forms_enabled', models.BooleanField(default=False)),
                ('learnset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocab.Learnset')),
            ],
        ),
    ]
