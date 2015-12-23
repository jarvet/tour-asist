# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0005_auto_20151121_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='master',
            field=models.ForeignKey(related_name='master', to='myweb.UserProfile'),
        ),
    ]
