from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
	path('', views.index, name='homepage'),

    path ('allmap', views.getalldata, name='allmap'),
    path ('skalaumkm', views.getskalajson, name='getskalajson'),
    path ('highomzetumkm', views.gethighomzet_umkm, name='gethighomzet_umkm'),
    path ('highasetumkm', views.gethighaset_umkm, name='gethighaset_umkm'),
    path ('bidangusahaumkm', views.bidush_umkm, name='bidush_umkm'),
    path ('koperasi/<int:kop_id>', views.getkopid, name='getkopid'),
    path ('umkm/<int:umkm_id>', views.getumkmid, name='getumkmid'),
    path ('berita/warta-kumkm', views.getallberita, name='getwartakumkm'),
    path ("berita/warta-kumkm/<series>/<article>", views.single_berita, name="single_berita"),
    path ("berita/warta-kumkm/<series>", views.list_series, name="list_series"),

	path ('berita/fakta-menarik', views.getallfakta, name='getfakta'),
    path ("berita/fakta-menarik/<series>/<article>", views.single_fakta, name="single_fakta"),
    path ("berita/fakta-menarik/<series>", views.list_series_fakta, name="list_series_fakta"),


	path ('berita/gallery', views.getallgallery, name='getgallery'),
    path ("berita/gallery/<series>/<article>", views.single_gallery, name="single_gallery"),
    path ("berita/gallery/<series>", views.list_series_gallery, name="list_series_gallery"),

    path ("regulasi/produk-hukum", views.front_regul_pdhk, name="list_produk_hukum"),
    path ("regulasi/rapat-koordinasi", views.front_rapat_koor, name="list_rapat_koordinasi"),
    path ("regulasi/paparan", views.front_paparan, name="list_paparan"),
    path ("hubungi-kami", views.contact_us, name="cont_us"),

    # path("<series>", views.series, name="series"),
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