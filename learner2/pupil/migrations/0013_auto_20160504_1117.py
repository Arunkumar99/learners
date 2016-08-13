# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0012_sessiondata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessiondata',
            name='user_id',
        ),
        migrations.AddField(
            model_name='sessiondata',
            name='user_name',
            field=models.CharField(default=datetime.datetime(2016, 5, 4, 5, 47, 26, 930972, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
