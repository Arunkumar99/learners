# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0005_auto_20160215_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ans', models.IntegerField()),
                ('hint', models.IntegerField()),
                ('time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name=b'user name')),
                ('password', models.CharField(max_length=30, verbose_name=b'user password')),
                ('emailid', models.CharField(max_length=50, verbose_name=b'emailid of user')),
                ('personal', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user_data',
            name='user',
            field=models.ForeignKey(to='pupil.User_info'),
        ),
    ]
