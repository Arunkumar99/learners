# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0016_auto_20160504_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessiondata',
            name='id',
        ),
        migrations.AlterField(
            model_name='sessiondata',
            name='user_id',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
