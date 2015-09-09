# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import geoposition.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('koupons', '0002_customuser_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='position',
            field=geoposition.fields.GeopositionField(default=datetime.datetime(2015, 8, 26, 15, 40, 53, 583343, tzinfo=utc), max_length=42),
            preserve_default=False,
        ),
    ]
