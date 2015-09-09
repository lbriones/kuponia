# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_auto_20150823_0628'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(blank=True, max_length=20, null=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('birthdate', models.DateField(null=True, verbose_name='Fecha de nacimiento', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Titulo del cupon.', max_length=255, verbose_name='Titulo', blank=True)),
                ('body', models.TextField(help_text='Descripcion del producto o servicio.', verbose_name='Contenido', blank=True)),
                ('discount', models.IntegerField(help_text='value del cupon', verbose_name='Descuento')),
                ('imagen', models.ImageField(default=b'img_coupons/default.jpg', upload_to=b'img_coupons/')),
                ('value', models.IntegerField(help_text='precio de producto o servicio', verbose_name='Precio')),
                ('promo', models.CharField(help_text='Titulo del cupon.', max_length=255, verbose_name='Promocion')),
                ('code', models.CharField(help_text='Si lo dejas vacio se genera un code random.', unique=True, max_length=30, verbose_name='codigo', blank=True)),
                ('type', models.CharField(max_length=20, verbose_name='Tipo', choices=[(b'servicios', b'Servicios'), (b'productos', b'Productos')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')),
                ('redeemed_at', models.DateTimeField(null=True, verbose_name='fecha de canje', blank=True)),
                ('valid_until', models.DateTimeField(help_text='Si lo dejas vacio no expirara', null=True, verbose_name='Valido hasta', blank=True)),
                ('slug', models.SlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
            },
        ),
    ]
