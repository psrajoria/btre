from .models import Realtor
from django.contrib import admin

# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_editable = ('is_mvp',)
    list_per_page = 10


admin.site.register(Realtor, RealtorAdmin)
