# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manage_expenses', '0003_auto_20150906_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userexpense',
            name='username',
        ),
        migrations.AddField(
            model_name='userexpense',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
