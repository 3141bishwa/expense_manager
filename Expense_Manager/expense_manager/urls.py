from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'/signup', views.signup, name='signup'),
    url(r'/login', views.login, name='login'),
    url(
        r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}
    ),
]