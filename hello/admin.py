from django.contrib import admin
from .models import COORD
from import_export.admin import ImportExportModelAdmin
# Register your models here.
#admin.site.register(COORD)

@admin.register(COORD)
class usrdet(ImportExportModelAdmin):
    pass
