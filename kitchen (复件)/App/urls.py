from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index', views.indexi, name='indexi'),
    url(r'^login', views.logini, name='logini'),
    url(r'^register', views.register, name='register'),
    url(r'^logout/$',views.logout,name='logout'),
    # url(r'^cart/$',views.cart,name='cart'),
    url(r'^info/$',views.info,name='info'),
    url(r'^order/$',views.order,name='order'),
    url(r'^orders/$',views.orders,name='orders'),
    url(r'^placeorder/$',views.placeorder,name='placeorder'),
    url(r'^site/$',views.site,name='site'),
    url(r'^detail/(?P<goodid>\w+)/$',views.detail,name='detail'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^check/$', views.check, name='check'),
    url(r'^change/$', views.change, name='change'),
    # url(r'^xiugai/$', views.xiugai, name='xiugai'),
    url(r'^password/$', views.password, name='password'),
    url(r'^passwords/$', views.passwords, name='passwords'),
    url(r'^send/$', views.send, name='send'),
    url(r'^addgood/$', views.addgood, name='goodadd'),
    url(r'^addcart/$', views.addcart, name='addcart'),
    url(r'^list/$', views.list, name='list'),


    # url(r'^gougou/$', views.gougou, name='gougou'),

]

