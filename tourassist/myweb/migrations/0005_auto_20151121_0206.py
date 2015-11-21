# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_auto_20151121_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveler',
            name='user',
        ),
        migrations.RemoveField(
            model_name='traveler',
            name='user_plans',
        ),
        migrations.AlterField(
            model_name='team',
            name='master',
            field=models.OneToOneField(related_name='master', to='myweb.UserProfile'),
        ),
        migrations.RemoveField(
            model_name='team',
            name='participant',
        ),
        migrations.AddField(
            model_name='team',
            name='participant',
            field=models.ManyToManyField(related_name='participant', to='myweb.UserProfile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='plan',
            field=models.OneToOneField(related_name='plan', to='myweb.Plan'),
        ),
        migrations.DeleteModel(
            name='Traveler',
        ),
    ]
