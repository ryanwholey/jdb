# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('value', models.IntegerField(default=600)),
                ('category', models.CharField(max_length=255)),
                ('air_date', models.DateField()),
                ('round', models.CharField(max_length=10)),
                ('show_number', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=500)),
                ('secret', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Team'),
        ),
        migrations.AddField(
            model_name='channel',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Team'),
        ),
    ]
