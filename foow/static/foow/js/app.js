
var $mainDiv = $('#mainBlogDiv');
var postNumber = 2;
var selectedList = 'desclist';
var lastPostNumber;

/// *********************************************************
/// When each post is clicked, it is opened to it's own page.
/// *********************************************************
function clickpost(postID){
	window.open("/post/"+postID, "_blank");
}

function sort(listName){
	selectedList = listName;
	$mainDiv.find('hr').remove();
	$mainDiv.find('.blog-post').fadeOut(500).remove();
	postNumber=2;
	postID = $('#'+selectedList+'').find('li[name=1]').html();
	lastPostNumber = parseInt($('#'+selectedList+'').find('li:last').attr('name'));
	getNextPost(postID);
}

/// *********************************************************
/// Gets the newest blog post from the API in JSON format
/// It then formats it into a blog-post template and fades
/// it into the main div
/// *********************************************************
function getNextPost(nextID){
	$spinner = $('.spinner:first').clone();
	$spinner.appendTo($mainDiv).show();
	$.ajax({
			type: 'GET',
			url: "/"+nextID,
			datatype: 'json',
			success: function(data){
				$.each(data, function(index, element){
					var dateObject = moment(element.fields.pub_date, "YYYYY-MM-DDTHH:mm:ssZ").format("MMM. DD, YYYY");
					var newElementText = "<div class='blog-post' name='"+element.pk+
						"' onclick='clickpost("+element.pk+")'>"+
						"<div class='blog-post-title'> "+ element.fields.blog_title + "</div>"+
						"<h3>"+element.fields.blog_subtitle+"</h3>"+
						"<p style='font-style: italic'>"+dateObject+"</p>"+
						"<div class='blog-description' style='font-size: small'>"+element.fields.blog_text+
						"</div>"+
					"</div><hr />";
					var $newElement = $("<div/>").html(newElementText).contents();
					$newElement.hide().appendTo($mainDiv).fadeIn(700);
					$('.spinner').remove();
				});
			}
		});
}

$(function(){
	//Display the first post with Date Descending being the default
	var postID = $('#'+selectedList+'').find('li[name=1]').html();
	lastPostNumber = parseInt($('#'+selectedList+'').find('li:last').attr('name'));
	getNextPost(postID);

	//Sort Oldest First Click
	$('#oldestFirst').on('click', function(){
		sort('asclist');
	});

	//Sort Newest First Click
	$('#newestFirst').on('click', function(){
		sort('desclist');
	});

	//Display More as you scroll
	$(window).scroll(function() {
    	if($(window).scrollTop() + $(window).height() == $(document).height()) {
    		if(postNumber <= lastPostNumber){
				postID = $('#'+selectedList+'').find('li[name='+postNumber+']').html();
	    		getNextPost(postID);
	        	postNumber = postNumber + 1;
        	}
   		}
	});

});

