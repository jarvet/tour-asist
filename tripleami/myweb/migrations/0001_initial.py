# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('starting', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('total_person', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
                ('user_plans', models.ManyToManyField(to='myweb.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sex', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('user', models.OneToOneField(verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='master',
            field=models.OneToOneField(to='myweb.Traveler'),
        ),
        migrations.AddField(
            model_name='team',
            name='participant',
            field=models.ForeignKey(related_name='participant', to='myweb.Traveler'),
        ),
        migrations.AddField(
            model_name='team',
            name='plan',
            field=models.OneToOneField(to='myweb.Plan'),
        ),
    ]
