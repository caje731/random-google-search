from django.conf.urls import include, url
from django.contrib import admin

import excel_download

urlpatterns = [
    # Examples:
    # url(r'^$', 'random_search.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^randomsearch/', include('excel_download.urls')),
]
