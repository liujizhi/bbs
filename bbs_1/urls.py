from django.conf.urls import include, url
from django.contrib import admin
import app01.urls
from app01 import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include(app01.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}), 
    url(r'^login/$', views.Login ),
    url(r'^acc_login/$', views.acc_login),
    url(r'^logout/$', views.logout_view),
    url(r'^register/$',views.register),
    
]
