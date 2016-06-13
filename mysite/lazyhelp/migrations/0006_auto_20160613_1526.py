# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lazyhelp', '0005_order_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='location',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pic2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pic3',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pic4',
        ),
    ]
