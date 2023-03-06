from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin

class KoperasiAdmin(ImportExportModelAdmin):
    pass

class KategoriIPAdmin(ImportExportModelAdmin):
    pass

class DpPatuhAdmin(ImportExportModelAdmin):
    model = DPPatuhModel
    list_display = ("kat_var", "ind_ukur", "dok_pendukung", "temuan")
    list_editable = ( "ind_ukur", "dok_pendukung", "temuan")
    pass #resource_classes = [BookResource]

admin.site.register(KoperasiModel, KoperasiAdmin)
admin.site.register(KategoriIPModel, KategoriIPAdmin)
admin.site.register(DPPatuhModel,DpPatuhAdmin)
admin.site.register(DetailDpPatuh)


# admin.site.register(Book, BookAdmin)