# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lazyhelp', '0003_auto_20160611_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
