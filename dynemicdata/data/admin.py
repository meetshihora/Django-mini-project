from django.contrib import admin
from data.models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'city')

admin.site.register(Data, DataAdmin)
# Register your models here.
