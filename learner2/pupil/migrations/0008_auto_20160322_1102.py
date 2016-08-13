# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0007_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='clue1',
            new_name='hint1',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='clue2',
            new_name='hint2',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='clue3',
            new_name='hint3',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='clue4',
            new_name='hint4',
        ),
    ]
