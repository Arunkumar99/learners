# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
                ('name', models.CharField(max_length=20, verbose_name=b'user name')),
                ('password', models.CharField(max_length=20, verbose_name=b'user password')),
                ('personal', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user_data',
            name='user',
            field=models.ForeignKey(to='pupil.User_info'),
        ),
    ]
