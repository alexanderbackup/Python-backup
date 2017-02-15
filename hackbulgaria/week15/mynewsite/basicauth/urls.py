from django.conf.urls import url
from basicauth import views


urlpatterns = [
    url(r'^login/$', views.login, name='login_page'),
    url(r'^logout/$', views.logout, name='logout_page'),
    url(r'^profile/$', views.profile, name='profile_page'),
    url(r'^register/$', views.registration, name='register_page'),
]
