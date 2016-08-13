# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0017_auto_20160504_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiondata',
            name='session_count',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='sessiondata',
            name='user_id',
            field=models.CharField(max_length=30),
        ),
    ]
