# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-27 03:59
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20170927_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='mapCenterLocation',
            field=django.contrib.gis.db.models.fields.PointField(null=True, max_length=40, srid=4326),
        ),
    ]