from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .models import KoperasiModel
from django.contrib.auth import get_user_model

class KoperasiResource(resources.ModelResource):

    id = Field(attribute='id', column_name='id')
    du_nakop = Field(attribute='du_nakop', column_name='Nama Koperasi')
    du_alkop = Field(attribute='du_alkop', column_name='Alamat Koperasi')
    du_bhkkop = Field(attribute='du_bhkkop', column_name='Badan Hukum Koperasi')
    rkp_lat = Field(attribute='rkp_lat', column_name='Latitude')
    rkp_long = Field(attribute='rkp_long', column_name='Longitude')
    rkp_nmpmlk = Field(attribute='rkp_nmpmlk', column_name='Nama Pemilik')
    rkp_nikpmlk = Field(attribute='rkp_nikpmlk', column_name='NIK Pemilik')
    rkp_nibkop = Field(attribute='rkp_nibkop', column_name='NIB Koperasi')

    # def after_import_instance(self, instance, new, **kwargs):
    #     instance.dt_user = kwargs['current_user']

    # def after_save_instance(self, instance, using_transactions, dry_run):
    #     # the model instance will have been saved at this point, and will have a pk
    #     print(instance.pk)
        
    class Meta:
        model = KoperasiModel
        fields = ("id","du_nakop", "du_alkop",'du_bhkkop','rkp_nmpmlk',
        'rkp_nikpmlk', 'rkp_nibkop','rkp_lat','rkp_long')
        # import_id_fields = ('id')
        use_natural_foreign_keys = True

    # def before_save_instance(self, instance, using_transactions, dry_run):
    #     # the model instance will have been saved at this point, and will have a pk

    #     field_name = self.get_field_name('id')
    #     field_name = instance.pk


    # def export(self, queryset=None, *args, **kwargs):
    #     queryset = get_user_model.objects.filter(agent=kwargs['agent'])
    #     return super(KoperasiResource, self).export(queryset, *args, **kwargs)

    # def export(self, queryset=None, *args, **kwargs):
    #     queryset = People.objects.filter(agent=kwargs['agent'])
    #     return super(PeopleResource, self).export(queryset, *args, **kwargs)