# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0021_auto_20160504_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('set_id', models.IntegerField(default=0)),
                ('question', models.TextField()),
                ('rans', models.IntegerField(default=0)),
                ('option1', models.CharField(max_length=30)),
                ('option2', models.CharField(max_length=30)),
                ('option3', models.CharField(max_length=30)),
                ('option4', models.CharField(max_length=30)),
                ('hint1', models.CharField(max_length=30)),
                ('hint2', models.CharField(max_length=30)),
                ('hint3', models.CharField(max_length=30)),
                ('hint4', models.CharField(max_length=30)),
            ],
        ),
    ]
