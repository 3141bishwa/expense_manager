# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_address',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
