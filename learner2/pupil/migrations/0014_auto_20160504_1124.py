# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0013_auto_20160504_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessiondata',
            old_name='csv_file',
            new_name='csv_file1',
        ),
        migrations.RemoveField(
            model_name='sessiondata',
            name='performance1',
        ),
        migrations.RemoveField(
            model_name='sessiondata',
            name='performance2',
        ),
        migrations.RemoveField(
            model_name='sessiondata',
            name='performance3',
        ),
        migrations.AddField(
            model_name='sessiondata',
            name='percent',
            field=models.IntegerField(default=0),
        ),
    ]
