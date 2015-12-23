# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_auto_20151121_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='end_time',
            field=models.DateField(default=datetime.datetime(2015, 11, 20, 17, 34, 37, 827000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='start_time',
            field=models.DateField(default=datetime.datetime(2015, 11, 20, 17, 34, 43, 570000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
