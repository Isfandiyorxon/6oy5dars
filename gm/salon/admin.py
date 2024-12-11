from django.contrib import admin

from .models import Cars, Brend
from django.utils.safestring import mark_safe
admin.site.register(Brend)
class Carsadmin(admin.ModelAdmin):
    list_display = ('pk','model','brend','color','max_speed','probeg','sotuvda_bormi','get_poto')
    list_display_links = ('model','pk')
    list_editable = ('sotuvda_bormi', 'brend')
    list_filter = ('brend','sotuvda_bormi')
    search_fields = ('pk','model')
    list_per_page = 5


    def get_poto(self,car):
        if car.photo:
            return mark_safe(f'<img src="{car.photo.url}" width="150px" />')
        else:
            return '-'

    get_poto.short_description="Rasmi"



admin.site.register(Cars, Carsadmin)

# Register your models here.
