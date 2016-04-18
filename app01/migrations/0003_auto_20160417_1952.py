# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_bbs_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='category',
            field=models.ForeignKey(default=1, to='app01.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bbs',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
