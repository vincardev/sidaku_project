from django.urls import path
from . import views

app_name = 'koperasi'

urlpatterns = [

	path('master', views.master_kop, name='master_kop'),
	path('add', views.add_kop, name='add_kop'),
	path('update/<int:kop_id>', views.upd_kop, name='upd_kop'),
	path('delete/<int:kop_id>', views.del_kop, name='del_kop'),
	
	path('addkeu/<int:kop_id>', views.add_keu_kop, name='add_keu_kop'),
	path('updkeu/<int:keu_id>/<int:kop_id>', views.upd_keu_kop, name='upd_keu_kop'),
	path('delkeu/<int:keu_id>/<int:kop_id>', views.del_keu_kop, name='del_keu_kop'),
    
    path ('getprodkop/<int:kop_id>', views.getjsonprodkop, name='prodkop'),

]