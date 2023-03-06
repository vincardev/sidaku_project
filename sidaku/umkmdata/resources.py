from import_export import resources, fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export.widgets import ForeignKeyWidget


from .models import BentukUsaha, BidangUsaha, UmkmModel
from django.contrib.auth import get_user_model

class UMKMResource(resources.ModelResource):

    id = Field(attribute='id', column_name='id')
    pu_noaggta = Field(attribute='pu_noaggta', column_name='Nomor Anggota')
    pu_nmpmlk = Field(attribute='pu_nmpmlk', column_name='Nama Lengkap')
    du_nmusha = Field(attribute='du_nmusha', column_name='Nama Usaha')
    pu_noktp = Field(attribute='pu_noktp', column_name='NIK')
    pu_aldmisi = Field(attribute='pu_aldmisi', column_name='Alamat (KTP)')
    du_alusha = Field(attribute='du_alusha', column_name='Alamat Usaha')
    pu_notlp = Field(attribute='pu_notlp', column_name='No. Telp')
    # du_btkusha = Field(attribute='du_btkusha', column_name='Bentuk Usaha')
    # du_bdgusha = Field(attribute='du_bdgusha', column_name='Bidang Usaha')
    du_btkusha = fields.Field(column_name='Bentuk Usaha', attribute='du_btkusha', widget=ManyToManyWidget(model=BentukUsaha,field='nama'))
    du_bdgusha = fields.Field(column_name='Bidang Usaha', attribute='du_bdgusha', widget=ManyToManyWidget(model=BidangUsaha,field='nama'))
    dtu_omzetthn    = Field(attribute='dtu_omzetthn', column_name='Omzet')
    dtu_totalaset    = Field(attribute='dtu_totalaset', column_name='Aset')
    dtu_skalausha    = Field(attribute='dtu_skalausha', column_name='Skala Usaha')
    du_lat    = Field(attribute='du_lat', column_name='Latitude')
    du_long   = Field(attribute='du_long', column_name='Longitude')
    pu_email = Field(attribute='pu_email', column_name='Email')
    du_thnbrdr = Field(attribute='du_thnbrdr', column_name='Tahun Berdiri')


    # def after_import_instance(self, instance, new, **kwargs):
    #     instance.dt_user = kwargs['current_user']

    # def after_save_instance(self, instance, using_transactions, dry_run):
    #     # the model instance will have been saved at this point, and will have a pk
    #     print(instance.pk)
        
    class Meta:
        model = UmkmModel
        fields = ("id","pu_noaggta", "pu_nmpmlk",'du_nmusha','pu_noktp',
        'pu_aldmisi', 'du_alusha','pu_notlp','du_btkusha','du_bdgusha','dtu_omzetthn',
        'dtu_totalaset','dtu_skalausha','du_lat','du_long','pu_email','du_thnbrdr')

        # widgets = {"du_bdgusha": {"field": "nama"}}
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