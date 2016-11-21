
var $mainDiv = $('#mainblogdiv');
var postNumber = 1;
var selectedList = 'desclist';
var lastPostNumber;
var maxPostsOnPage = 5;
var pageNumber = 1;
var numPages;
var pageCount = 0;

function populateNew(){
	var postID = $('#'+selectedList+'').find('li[name='+postNumber+']').html();
	$.ajax({
			type: 'GET',
			url: "/"+postID,
			datatype: 'json',
			success: function(data){
				$.each(data, function(index, element){
					var dateObject = moment(element.fields.pub_date, "YYYYY-MM-DDTHH:mm:ssZ").format("MMM. DD, YYYY");
					var newElementText = "<div class='post-preview' name = '"+element.pk+"'>"+
                    "<a href='/post/"+element.pk+"'>"+
                        "<h2 class='post-title'>"+
                            element.fields.blog_title+
                        "</h2>"+
                        "<h3 class='post-subtitle'>"+
                            element.fields.blog_subtitle+
                        "</h3>"+
                    "</a>"+
                    "<p class='post-meta'>Posted on "+dateObject+"</p>"+
	                "</div>"+
	                "<hr />";
					var $newElement = $("<div/>").html(newElementText).contents();
					$newElement.hide().appendTo($mainDiv).fadeIn(1200);
					postNumber = postNumber + 1;
					pageCount = pageCount + 1;
					if(postNumber <= lastPostNumber && pageCount < maxPostsOnPage){
						populateNew();
					}
				});
			}
		});
}


function sort(listName){
	selectedList = listName;
	clearPage();
	postNumber=1;
	pageNumber=1;
	pageCount = 0;
	postID = $('#'+selectedList+'').find('li[name=1]').html();
	lastPostNumber = parseInt($('#'+selectedList+'').find('li:last').attr('name'));
	populateNew();
	$('li.next').fadeIn(500);
	$('li.previous').fadeOut(500).hide();
}

function clearPage(){
	$mainDiv.find('hr').remove();
	$mainDiv.find('.post-preview').fadeOut(500).remove();

}
function pageUp(){
	//increment the page number
	pageNumber = pageNumber + 1;
	postNumber = (pageNumber - 1) * maxPostsOnPage + 1;
	pageCount = 0;
	clearPage();
	populateNew();
	$('li.previous').fadeIn(500);

	if(pageNumber == numPages){
		$('li.next').fadeOut(500).hide();
	}
}
function pageDown(){
	pageNumber = pageNumber - 1;
	postNumber = (pageNumber - 1) * maxPostsOnPage + 1;
	pageCount = 0;
	clearPage();
	populateNew();
	$('li.next').fadeIn(500);

	if(pageNumber == 1){
		$('li.previous').fadeOut(500).hide();
	}
}

$(function(){

	//Sort Oldest First Click
	$('#oldestFirst').on('click', function(){
		sort('asclist');
	});

	//Sort Newest First Click
	$('#newestFirst').on('click', function(){
		sort('desclist');
	});

	$('li.next').on('click', function(){
		pageUp();
	});
	$('li.previous').on('click', function(){ 
		pageDown();
	});

	lastPostNumber = parseInt($('#'+selectedList+'').find('li:last').attr('name'));
	numPages = Math.floor($('#'+selectedList+'').find('li').length/maxPostsOnPage);
	if($('#'+selectedList+'').find('li').length%maxPostsOnPage != 0)
		numPages = numPages + 1;
	//alert(numPages);
	populateNew();
	$('li.previous').hide();
});