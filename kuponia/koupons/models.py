import random
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import AbstractUser
from geoposition.fields import GeopositionField
import string
COUPON_TYPES = (
    ('servicios', 'Servicios'),
    ('productos', 'Productos'),
)
SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

code_LENGTH = 15

code_CHARS = string.ascii_letters+string.digits

SEGMENTED_codeS = False
SEGMENT_LENGTH = 4
SEGMENT_SEPARATOR = "-"


class Coupon(models.Model):
    title = models.CharField(_("Titulo"), max_length=255, blank=True, help_text=_("Titulo del cupon."))
    body = models.TextField(_("Contenido"), blank=True, help_text=_("Descripcion del producto o servicio."))
    position = GeopositionField()
    address = models.CharField(_("Direccion"), max_length=255, help_text=_("Direccion de canje"))
    discount = models.IntegerField(_("Descuento"), help_text=_("value del cupon"))
    imagen = models.ImageField(upload_to = 'img_coupons/', default = 'img_coupons/default.jpg')
    value = models.IntegerField(_("Precio"), help_text=_("precio de producto o servicio"))
    promo = models.CharField(_("Promocion"), max_length=255, help_text=_("Titulo del cupon."))
    code = models.CharField(_("codigo"), max_length=30, unique=True, blank=True, help_text=_("Si lo dejas vacio se genera un code random."))
    type = models.CharField(_("Tipo"), max_length=20, choices=COUPON_TYPES)
    created_at = models.DateTimeField(_("fecha creacion"), auto_now_add=True)
    redeemed_at = models.DateTimeField(_("fecha de canje"), blank=True, null=True)
    valid_until = models.DateTimeField(_("Valido hasta"), blank=True, null=True, help_text=_("Si lo dejas vacio no expirara"))
    slug = models.SlugField(editable=False, unique=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = Coupon.generate_code()
            self.slug = unique_slugify(self.title)
        super(Coupon, self).save(*args, **kwargs)

    def expired(self):
        return self.valid_until is not None and self.valid_until < timezone.now()

    @classmethod
    def generate_code(cls, prefix="", segmented=SEGMENTED_codeS):
        code = "".join(random.choice(code_CHARS) for i in range(code_LENGTH))
        if segmented:
            code = SEGMENT_SEPARATOR.join([code[i:i+SEGMENT_LENGTH] for i in range(0, len(code), SEGMENT_LENGTH)])
            return prefix + code
        else:
            return prefix + code

#quita propiedad de username eliminar index de username desde la base de datos
User._meta.get_field('username')._unique = False

# AbstractUser already has the following fields and others.
# username, first_name, last_name
# email, password, groups
SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class CustomUser(AbstractUser):
    gender = models.CharField(choices=SEXO, max_length=20, blank=True, null=True)
    birthdate = models.DateField(_("Fecha de nacimiento"), blank=True, null=True)
    favorites = models.ManyToManyField(Coupon, related_name='favorited_by')
    #favorites = models.ManyToManyField(Coupon, related_name='favorited_by')
    # to enforce that you require email field to be associated with
    # every user at registration
    REQUIRED_FIELDS = ["email"]
