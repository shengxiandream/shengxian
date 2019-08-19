from django.conf.urls import url
from Admin import views

urlpatterns = [
    url(r'^$',views.login,name='login'),
    # url(r'^fu/$',views.fu,name='fu')
    url(r'^index/$',views.index,name='index'),
    url(r'^index/(?P<did>\d+)/$', views.index, name='index1'),
    url(r'^index/(?P<did>\d+)/(?P<page>\d+)/$',views.index,name='index2'),
    # url(r'^index/?id=(\d+)/(\d+)/$',views.index,name='index1'),
    url(r'^zhaohui/$',views.zhaohui,name='zhaohui'),
    url(r'^youjian/$',views.youjian,name='youjian'),
    url(r'^upload/$',views.upload,name='upload'),
    url(r'^jinyong/$',views.jinyong,name='jinyong'),
    url(r'^yunyong/$', views.yunyong, name='yunyong'),
    url(r'^xiashang/$', views.xiashang, name='xiashang'),
    url(r'^shangshang/$', views.shangshang, name='shangshang'),
    url(r'^shanshang/$', views.shanshang, name='shanshang'),
    url(r'^xiushang/(?P<id>\d+)/$', views.xiushang, name='xiushang'),
    url(r'^xiaoguan/$', views.xiaoguan, name='xiaoguan'),


]

handler404 = views.page_not_found
handler500 = views.page_inter_error