# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0010_auto_20160405_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='set_id',
            field=models.IntegerField(default=0),
        ),
    ]
