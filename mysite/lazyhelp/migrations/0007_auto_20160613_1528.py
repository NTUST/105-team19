# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lazyhelp', '0006_auto_20160613_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(related_name='uid_b', to='lazyhelp.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='saler',
            field=models.ForeignKey(related_name='uid_s', to='lazyhelp.User'),
            preserve_default=True,
        ),
    ]
