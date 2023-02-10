
from datetime import datetime

from companysetup.models import CompanySetupModel
from userprofile.models import UserProfile

def GetCompany(request):
    tables_company = CompanySetupModel.objects.get()

    datetoday = datetime.today().weekday()
    myprof = None
    if request.user.is_authenticated :
        myprof, __  = UserProfile.objects.get_or_create(user=request.user)

    return {
            "tables_company" :tables_company,
            "weekday" : datetoday,
            "tables_profile" : myprof,
        }