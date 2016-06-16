# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lazyhelp', '0007_auto_20160613_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bulid_date',
            field=models.DateField(default=datetime.datetime(2016, 6, 16, 14, 30, 56, 310249, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
