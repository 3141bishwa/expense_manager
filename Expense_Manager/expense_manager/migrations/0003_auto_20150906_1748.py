# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0002_auto_20150906_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExpense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'', max_length=200)),
                ('cost', models.FloatField(default=0)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('purchase_date', models.CharField(max_length=100)),
                ('purchase_store', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
