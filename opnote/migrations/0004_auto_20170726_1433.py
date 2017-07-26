# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opnote', '0003_auto_20170716_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationnote',
            name='dvt_aspirin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='operationnote',
            name='dvt_heparin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='operationnote',
            name='dvt_pnematic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='operationnote',
            name='dvt_ted_stockings',
            field=models.BooleanField(default=False),
        ),
    ]
