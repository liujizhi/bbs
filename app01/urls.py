from django.conf.urls import include, url

import views
urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'',include(app01.urls)),
    url(r'^$',views.index),
    url(r'^detail/(\d+)/$',views.bbs_detail),
    url(r'^sub_comment',views.sub_comment),
    url(r'^bbs_pub/$',views.bbs_pub),
    url(r'^bbs_sub/$',views.bbs_sub),
    url(r'^category/(\d+)/$',views.category),

]
