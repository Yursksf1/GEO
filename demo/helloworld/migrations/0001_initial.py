# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0005_rename_flowcls'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorldProcess',
            fields=[
                ('process_ptr', models.OneToOneField(primary_key=True, serialize=False, to='viewflow.Process', auto_created=True, parent_link=True)),
                ('text', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
