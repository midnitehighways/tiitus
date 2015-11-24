# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='firstname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='lastname',
            field=models.CharField(max_length=50),
        ),
    ]
