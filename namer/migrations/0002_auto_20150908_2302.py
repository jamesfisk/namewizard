# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('namer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matrix',
            old_name='probabilty_matrix',
            new_name='probability_matrix',
        ),
    ]
