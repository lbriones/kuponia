from django.contrib import admin
from .models import Coupon, CustomUser
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

@admin.register(Coupon)
class CouponAdmin(MarkdownModelAdmin):
    pass
    list_display = ['title', 'address', 'type', 'value', 'valid_until']
    list_filter = ['type',]
    #raw_id_fields = ('user',)
    search_fields = ['title'] #('user__username', 'user__email', 'code', 'value')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
    #list_display = ['user']

# Register your models here.
