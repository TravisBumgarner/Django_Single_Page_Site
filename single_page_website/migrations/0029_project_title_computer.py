# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0028_auto_20160924_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title_computer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
