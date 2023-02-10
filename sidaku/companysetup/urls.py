from django.urls import path
from . import views 

app_name = 'companysetup'

urlpatterns = [
	path('add', views.add_compsetup, name='newsetting'),
	path('update/<int:comp_id>', views.upd_compsetup, name='updsetting'),
]