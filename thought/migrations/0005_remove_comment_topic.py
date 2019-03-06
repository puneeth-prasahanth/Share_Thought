# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thought', '0004_auto_20190228_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Topic',
        ),
    ]
