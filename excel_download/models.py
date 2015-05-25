from django.db import models

# Create your models here.

class SearchString(models.Model):

	words = models.TextField(blank=False, unique=True)

	# Timestamps
	created_at	=	models.DateTimeField(auto_now_add=True) 
	updated_at	=	models.DateTimeField(auto_now=True)



class SearchResult(models.Model):

	searchstring = models.ForeignKey(SearchString, related_name='keywords', related_query_name='results')
	result_title = models.CharField(blank=False, unique=True, max_length=200)
	result_url 	 = models.TextField(blank=False)
	
	# Timestamps
	created_at	=	models.DateTimeField(auto_now_add=True) 
	updated_at	=	models.DateTimeField(auto_now=True)