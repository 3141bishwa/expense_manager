from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'/signup', views.signup, name='signup'),
    url(r'/login', views.login, name='login'),
    url(
        r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}
    ),
    url(r'^getallusers',views.getallusers, name='getallusers'),
    url(r'update_expense',views.update_expense, name = 'update_expense'),
    url(r'get_expenses', views.get_expenses, name="get_expenses")
]