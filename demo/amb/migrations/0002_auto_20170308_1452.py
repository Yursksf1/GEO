# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambprocess',
            name='text2',
        ),
        migrations.AddField(
            model_name='ambprocess',
            name='email',
            field=models.EmailField(max_length=254, default=False),
        ),
    ]
