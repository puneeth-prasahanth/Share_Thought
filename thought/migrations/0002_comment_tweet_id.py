# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thought', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tweet_id',
            field=models.IntegerField(default=0),
        ),
    ]
