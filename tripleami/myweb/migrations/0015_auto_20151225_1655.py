# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0014_auto_20151127_0350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['start_time', 'end_time', '-create_time']},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default=b'http://tripleami-media.stor.sinaapp.com/image/default.jpg', upload_to=b'./image/'),
        ),
    ]
