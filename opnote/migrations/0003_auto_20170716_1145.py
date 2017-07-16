# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opnote', '0002_auto_20170716_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffmember',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='staffmember',
            name='forname',
        ),
        migrations.RemoveField(
            model_name='staffmember',
            name='surname',
        ),
        migrations.AddField(
            model_name='staffmember',
            name='name',
            field=models.CharField(default='bart', unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
