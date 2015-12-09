# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_company_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='details',
            field=models.TextField(blank=True),
        ),
    ]
