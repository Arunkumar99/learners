# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0011_questions_set_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('session_count', models.IntegerField(default=0)),
                ('result', models.CharField(max_length=10)),
                ('level', models.IntegerField(default=0)),
                ('performance1', models.ImageField(upload_to=b'')),
                ('performance2', models.ImageField(upload_to=b'')),
                ('performance3', models.ImageField(upload_to=b'')),
                ('csv_file', models.FileField(upload_to=b'')),
            ],
        ),
    ]
