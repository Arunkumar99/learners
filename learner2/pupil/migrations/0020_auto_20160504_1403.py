# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0019_auto_20160504_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessiondata',
            name='sessiondata',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='sessiondata',
            name='session_count',
            field=models.IntegerField(default=1),
        ),
    ]
