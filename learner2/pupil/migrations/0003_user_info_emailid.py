# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0002_auto_20160213_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='emailid',
            field=models.CharField(default=0, max_length=50, verbose_name=b'emailid of user'),
            preserve_default=False,
        ),
    ]
