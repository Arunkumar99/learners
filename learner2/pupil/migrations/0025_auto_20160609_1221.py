# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0024_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
