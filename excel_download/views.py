from django.shortcuts import render_to_response
from django.http import JsonResponse, HttpResponse
import json
from util import gcs
from models import SearchString, SearchResult
from import_export import resources
# Create your views here.

GET 	= "GET"
POST	= "POST"
PUT		= "PUT"
DELETE 	= "DELETE"

# For exporting data into Excel
class ResultResource(resources.ModelResource):
	class Meta:
		model = SearchResult
			
# View functions
def random_search(request):
	return render_to_response('random_search.html')

# AJAX handler for triggering a search on google
def search_google(request):
	if(request.method==GET):
		keywords = request.GET["keywords"]
		response = gcs.search(q=keywords)
		
		SearchString.objects.filter(words=keywords).delete()
		searchstring = SearchString(words=keywords)
		searchstring.save()

		for item in response['items']:
			searchresult = SearchResult(searchstring=searchstring, result_title=item['htmlTitle'], result_url=item['link'])
			searchresult.save()

		return JsonResponse({'search_id': searchstring.id , 'data':response})

# AJAX handler for converting json data to excel
def excel_download(request):
	if (request.method == GET):
		
		search_id = request.GET["search_id"]
		srchstr = SearchString.objects.get(pk=search_id)
		dataset = ResultResource().export(SearchResult.objects.filter(searchstring=srchstr))
		
		response = HttpResponse(dataset.csv, content_type="application/ms-excel")
		response['Content-Disposition'] = 'attachment; filename="results.csv"'
		return response



		