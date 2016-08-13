# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0015_auto_20160504_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessiondata',
            old_name='user_name',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='sessiondata',
            name='csv_file1',
        ),
        migrations.RemoveField(
            model_name='sessiondata',
            name='csv_file2',
        ),
        migrations.RemoveField(
            model_name='sessiondata',
            name='csv_file3',
        ),
    ]
