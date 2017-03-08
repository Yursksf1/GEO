# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0005_rename_flowcls'),
    ]

    operations = [
        migrations.CreateModel(
            name='ambProcess',
            fields=[
                ('process_ptr', models.OneToOneField(serialize=False, auto_created=True, to='viewflow.Process', primary_key=True, parent_link=True)),
                ('text', models.CharField(max_length=150)),
                ('text2', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
