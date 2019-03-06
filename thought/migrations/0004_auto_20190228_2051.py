# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thought', '0003_auto_20190228_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tweet_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
