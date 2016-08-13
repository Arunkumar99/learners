# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0006_auto_20160215_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=30)),
                ('option2', models.CharField(max_length=30)),
                ('option3', models.CharField(max_length=30)),
                ('option4', models.CharField(max_length=30)),
                ('clue1', models.CharField(max_length=30)),
                ('clue2', models.CharField(max_length=30)),
                ('clue3', models.CharField(max_length=30)),
                ('clue4', models.CharField(max_length=30)),
            ],
        ),
    ]
