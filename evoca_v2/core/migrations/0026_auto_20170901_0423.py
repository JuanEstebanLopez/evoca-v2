# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20170901_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='tags',
            field=models.ManyToManyField(through='core.RecordTag', to='core.Tag'),
        ),
        migrations.AddField(
            model_name='recordtag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recordtag',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recordtag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]