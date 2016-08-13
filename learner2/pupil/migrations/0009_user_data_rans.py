# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0008_auto_20160322_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='rans',
            field=models.IntegerField(default=0),
        ),
    ]
