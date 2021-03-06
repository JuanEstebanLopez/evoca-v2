# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_record_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('uniqueID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('related_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_channel', to='core.Channel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='channeltag',
            name='related_channel',
        ),
        migrations.RemoveField(
            model_name='record',
            name='tags',
        ),
        migrations.DeleteModel(
            name='ChannelTag',
        ),
        migrations.AddField(
            model_name='recordtag',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_related_record', to='core.Record'),
        ),
        migrations.AddField(
            model_name='recordtag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_tag', to='core.Tag'),
        ),
    ]
