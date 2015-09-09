# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koupons', '0003_coupon_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='address',
            field=models.CharField(default='santiago, chile', help_text='Direccion de canje', max_length=255, verbose_name='Direccion'),
            preserve_default=False,
        ),
    ]
