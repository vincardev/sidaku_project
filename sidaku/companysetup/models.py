from django.db import models

# Create your models here.
class CompanySetupModel(models.Model):
    compName       = models.CharField(max_length=100)
    compLogo       = models.ImageField(upload_to= 'company/logo/', null=True, blank=True)
    compDesc       = models.TextField(max_length=350, null=True)  
    compAddr       = models.TextField(max_length=350,null=True, blank=True)

    compPhone      = models.CharField(max_length=30, blank=True, null=True)
    compEmail      = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    compFb         = models.CharField(max_length=150)
    compIg         = models.CharField(max_length=150)
    compWeb        = models.CharField(max_length=150)

    compAdm1       = models.CharField(max_length=30, blank=True, null=True)
    compAdm2       = models.CharField(max_length=30, blank=True, null=True)
    compAdmNm1     = models.CharField(max_length=30, blank=True, null=True)
    compAdmNm2     = models.CharField(max_length=30, blank=True, null=True)
    compAdmFt1     = models.ImageField(upload_to= 'company/adm/', null=True, blank=True)
    compAdmFt2     = models.ImageField(upload_to= 'company/adm/', null=True, blank=True)


    partName       = models.CharField(max_length=100)
    partLogo       = models.ImageField(upload_to= 'partner/logo/', null=True, blank=True)
    partDesc       = models.TextField(max_length=350, null=True)  
    partAddr       = models.TextField(max_length=350,null=True, blank=True)


    created_by      = models.CharField(max_length=25,blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=25,blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.compName



class SupportCenterModel(models.Model):
    scName       = models.CharField(max_length=100)
    scSubjek     = models.CharField(max_length=100)
    scPhone      = models.CharField(max_length=30)
    scEmail      = models.EmailField(max_length=255)
    scMsgs       = models.TextField(max_length=500)  

    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.scName

    class Meta:
        db_table = 'support_center_data'
        verbose_name_plural = 'support_center_data'