# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0018_auto_20160504_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiondata',
            name='session_count',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
        ),
    ]
