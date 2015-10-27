# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151027_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('advertisement_short', models.CharField(max_length=500)),
                ('advertisement_full', models.CharField(max_length=2000, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='description',
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='city',
            field=models.CharField(default=b'Helsinki', max_length=50),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='country',
            field=models.CharField(default=b'Finland', max_length=50),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='description_full',
            field=models.CharField(max_length=2000, blank=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='description_short',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='interests',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'photos'),
        ),
    ]
