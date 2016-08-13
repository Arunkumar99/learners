# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0009_user_data_rans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='rans',
        ),
        migrations.AddField(
            model_name='questions',
            name='rans',
            field=models.IntegerField(default=0),
        ),
    ]
