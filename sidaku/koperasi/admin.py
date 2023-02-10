from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

class KoperasiAdmin(ImportExportModelAdmin):
    pass

admin.site.register(KoperasiModel, KoperasiAdmin)