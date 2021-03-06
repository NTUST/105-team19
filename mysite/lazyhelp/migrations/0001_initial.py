# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('pic1', models.ImageField(height_field=500, upload_to=b'', width_field=500)),
                ('pic2', models.ImageField(height_field=500, upload_to=b'', width_field=500)),
                ('pic3', models.ImageField(height_field=500, upload_to=b'', width_field=500)),
                ('pic4', models.ImageField(height_field=500, upload_to=b'', width_field=500)),
                ('deadline', models.DateField()),
                ('point_to_b', models.IntegerField()),
                ('point_to_s', models.IntegerField()),
                ('status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('account', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('point', models.DecimalField(decimal_places=0, max_digits=10)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user_profile_b', to='lazyhelp.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='saler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user_profile_s', to='lazyhelp.User'),
        ),
    ]
