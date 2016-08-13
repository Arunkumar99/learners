# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0014_auto_20160504_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessiondata',
            name='csv_file2',
            field=models.FileField(default=0, upload_to=b''),
        ),
        migrations.AddField(
            model_name='sessiondata',
            name='csv_file3',
            field=models.FileField(default=0, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='sessiondata',
            name='csv_file1',
            field=models.FileField(default=0, upload_to=b''),
        ),
    ]
