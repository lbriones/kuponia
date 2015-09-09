# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='koupons.Coupon'),
        ),
    ]
