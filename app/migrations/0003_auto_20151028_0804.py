# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_company_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AddField(
            model_name='position',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 28, 8, 4, 9, 981756, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
