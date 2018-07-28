from django.conf.urls import re_path
from. import views
from. import views_cbv
urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)$', views.mysum),
    re_path(r'hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)$', views.hello),
    re_path(r'^list1/$',views.post_list1),
    re_path(r'^list2/$',views.post_list2),
    re_path(r'^list3/$',views.post_list3),
    re_path(r'^excel_down/$',views.excel_download),

    re_path(r'^cbv/list1/$',views.post_list1),
    re_path(r'^cbv/list2/$',views.post_list2),
    #re_path(r'^cbv/list3/$',views.post_list3),
    #re_path(r'^cbv/excel_down/$',views.excel_download),
] 
