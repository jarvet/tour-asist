# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0006_auto_20151121_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['-create_time', 'start_time', 'end_time']},
        ),
        migrations.AddField(
            model_name='plan',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2015, 11, 24, 15, 59, 13, 326000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
