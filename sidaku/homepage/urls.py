from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
	path('', views.index, name='homepage'),

    path ('allmap', views.getalldata, name='allmap'),
    path ('koperasi/<int:kop_id>', views.getkopid, name='getkopid'),
    path ('umkm/<int:umkm_id>', views.getumkmid, name='getumkmid'),
	# path('add', views.add_packages, name='add_packages'),
	# path('update/<int:pack_id>', views.update_packages, name='update_packages'),
	# path('delete/<int:pack_id>', views.del_packages, name='del_packages'),

	# path('rates/delete/<int:pack_id>/<int:prates_id>', views.del_packrates, name='del_packrates'),
	# path('rates/get/<int:prates_                                                                                                                          id>', views.getpackrates, name='getpackrates'),
	# path('rates/add/<int:pack_id>', views.addpackrates, name='addpackrates'),
	# path('rates/update/<int:pack_id>', views.updatepackrates, name='updatepackrates'),
	# path('rates/update/<int:pack_id>/<int:prates_id>', views.updatepackrates, name='updatepackrates'),
	# path('rates/getall/<int:pack_id>', views.gettablepackrates, name='gettablepackrates'),
	
	# path('detail_item/add', views.addetailitempack, name='addetailitempack'),
	# path('detail_item/delete/<int:pack_id>/<int:dtp_id>', views.deldetailitempack, name='deldetailitempack'),

	# path('detail_item/update/<int:dtp_id>', views.UpdateDetailItemRates, name='UpdateDetailItemRates'),


	# path('detail_room/add', views.addetailroompack, name='addetailroompack'),
	# path('detail_room/delete/<int:pack_id>/<int:dtp_id>', views.deldetailroompack, name='deldetailroompack'),

]