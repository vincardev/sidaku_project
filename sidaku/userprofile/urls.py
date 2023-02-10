from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [

    path('self_profile/', views.ProfileView.as_view(), name='selfprofile'),

	path('master', views.master_userp, name='master_userp'),
	path('add', views.add_userp, name='add_userp'),
	path('update/<int:user_id>', views.update_userp, name='update_userp'),
	path('delete/<int:user_id>', views.del_userp, name='del_userp'),
	# path('', views.index, name='userprofile'),
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