# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0004_auto_20150906_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userexpense',
            name='user',
        ),
        migrations.AddField(
            model_name='userexpense',
            name='expense_poster',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='userexpense',
            name='username',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
