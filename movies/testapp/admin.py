from django.contrib import admin
from testapp.models import movies_db
class moviesadmin(admin.ModelAdmin):
    list_display = ['name','actor','actress','year','rating']
admin.site.register(movies_db,moviesadmin)

