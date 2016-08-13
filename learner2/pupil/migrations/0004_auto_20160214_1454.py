# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0003_user_info_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='name',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'user name'),
        ),
    ]
