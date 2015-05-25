$(document).ready(function(){

	$('#srchsimple').click(function(e){
		var keywords = $('#keywords').val();

		// If nothing has been entered, do nothing
		if(keywords.length <1) return;

		$.ajax({
            url: "/randomsearch/keywords/search?keywords="+encodeURIComponent(keywords),
            type: 'GET',
            dataType: 'json',
                context: e,    // will be used as "this" variable in promise hooks
                data:{},
                beforeSend: function(xhr){
                    $('#wait').css('display', 'block');
                    $("#table-results").html('');
                    $(e.target).button('loading');
                }
            })
        	.done(function(data, textStatus, jqXHR){
        		var items = data['data']['items'];
	            if (items) {
	            	var table_rows = '';
	            	var header = "<tr>"+
	        						"<th> Sr. No.</th>"+
	        						"<th> Title </th>"+
	        						"<th> URL </th>"+
	        					"</tr>";

	        		table_rows += header;

	            	for (var i = 0; i < items.length; i++) {

	            		var item = items[i];
	            		var link = item['link'];
	            		var title= item['htmlTitle'];

	            		var row = 	"<tr>"+
	            						"<td>"+(i+1)+"</td>"+
	            						"<td>"+title+"</td>"+
	            						"<td>"+link+"</td>"+
	            					"</tr>";
	            		table_rows +=row;
	            	}
	            	$("#table-results").append($(table_rows));
	            	
	            	var alert = $('<div class="alert alert-success" role="alert">Downloading excel file with results for <strong>'+keywords+'</strong></div>');
	            	$('body').prepend(alert);
	            	
	            	// Download a csv file
	            	window.open("/randomsearch/download?search_id="+data['search_id']);
	            	alert.remove();

	    
            }
        })
		.fail(function(jqXHR, textStatus, errorThrown){
		    alert('Failed: '+JSON.parse(jqXHR.responseText).msg);
		})
		.always(function(){
		    $('#wait').css('display', 'none');
		    $(e.target).button('reset');
		});
	});

	$('#srchrandom').click(function(e){
		$('#keywords').val(words(4).join(' '));
		$('#srchsimple').click();
	});
});