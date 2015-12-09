# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contact_email',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
