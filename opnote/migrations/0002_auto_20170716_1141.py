# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0031_auto_20170715_1437'),
        ('opnote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnaestheticType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AsaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CancerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperationNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('dvt_heparin', models.BooleanField()),
                ('dvt_ted_stockings', models.BooleanField()),
                ('dvt_pnematic', models.BooleanField()),
                ('dvt_aspirin', models.BooleanField()),
                ('antibiotics', models.CharField(max_length=40)),
                ('indication', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('incision', models.CharField(max_length=20)),
                ('findings', models.TextField()),
                ('procedure', models.TextField()),
                ('lead_surgeon_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('lead_anaesthetist_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('cancer_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('asa_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('anaesthetic_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('urgency_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('anaesthetic_fk', models.ForeignKey(blank=True, to='opnote.AnaestheticType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=20)),
                ('forname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='operationnote',
            name='anaesthetist',
            field=models.ManyToManyField(related_name='operationnote_anaesthetist', to='opnote.StaffMember'),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='asa_fk',
            field=models.ForeignKey(blank=True, to='opnote.AsaType', null=True),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='assistant',
            field=models.ManyToManyField(related_name='operationnote_assistant', to='opnote.StaffMember'),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='cancer_fk',
            field=models.ForeignKey(blank=True, to='opnote.CancerType', null=True),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='created_by',
            field=models.ForeignKey(related_name='created_opnote_operationnote_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='episode',
            field=models.ForeignKey(to='opal.Episode'),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='lead_anaesthetist_fk',
            field=models.ForeignKey(related_name='operationnote_lead_anaesthetist', blank=True, to='opnote.StaffMember', null=True),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='lead_surgeon_fk',
            field=models.ForeignKey(related_name='operationnote_lead_surgeon', blank=True, to='opnote.StaffMember', null=True),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='surgeon',
            field=models.ManyToManyField(related_name='operationnote_surgeon', to='opnote.StaffMember'),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_opnote_operationnote_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='operationnote',
            name='urgency_fk',
            field=models.ForeignKey(blank=True, to='opnote.Urgency', null=True),
        ),
    ]
