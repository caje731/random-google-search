from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^keywords$' 		, views.random_search	, name='techtree:random_search'),
	url(r'^keywords/search$', views.search_google	, name='techtree:search_google'),
	url(r'^download$' 		, views.excel_download	, name='techtree:excel_download'),
]