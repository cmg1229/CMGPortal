
var $mainDiv = $('#mainBlogDiv');



var nextID;

function clickPost(postID){
	window.open("/post/"+postID, "_blank");
}

$(function(){
	//Get the first blogpost
	firstbp = $('.blog-post:first');
	//Convert the name attribute to a number
	nextID = +(firstbp.attr("name")) - 1;



	//Display more posts as you scroll
	$(window).scroll(function() {
    	if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
    		if(nextID > 0){
	    		$.ajax({
	    			type: 'GET',
	    			url: "/"+nextID,
	    			datatype: 'json',
	    			success: function(data){
	    				$.each(data, function(index, element){
	    					var newElementText = "<hr /><div class='blog-post' name='"+element.fields.post_id+" onclick='clickPost("+element.fields.post_id+")'>"+
	    						"<div class='blog-post-title'> "+ element.fields.blog_title + "</div>"+
	    						"<h2>"+element.fields.blog_subtitle+"</h2>"+
	    						"<p style='font-style: italic'>"+element.fields.pub_date+"</p>"+
								"<div class='blog-description' style='font-size: small'>"+element.fields.blog_text+
								"</div>"+
	    					"</div>";
	    					var $newElement = $("<div/>").html(newElementText).contents();
	    					$newElement.appendTo($mainDiv).fadeIn('slow');
	    				});
	    			}
	    		});
	        	nextID = nextID - 1;
        	}
   		}
	});


});

