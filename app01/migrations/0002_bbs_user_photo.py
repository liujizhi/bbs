# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(default=b'./upload_imgs/', upload_to=b'./upload_imgs/'),
        ),
    ]
