from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Expense_Manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('manage_expenses.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
