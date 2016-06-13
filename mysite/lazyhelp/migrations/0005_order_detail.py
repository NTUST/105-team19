# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lazyhelp', '0004_auto_20160613_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='detail',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
