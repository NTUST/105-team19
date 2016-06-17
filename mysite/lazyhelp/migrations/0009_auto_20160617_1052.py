# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lazyhelp', '0008_order_bulid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pic1',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
