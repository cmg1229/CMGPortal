
$mainDiv = $('#mainBlogDiv');
$blogTemplate = $('#blogTemplate');

$(function(){
	$.ajax({
		type: 'GET',
		url: '/foow/allposts', 
		success: function(postDatas){
			$.each(postDatas, function(index, postData){
				var template = document.getElementById("blogTemplate");
				var clone = template.content.cloneNode(true);
				var $temp = $(clone);
				alert($temp.html());
			});
		},
		error: function(){
			alert('Ajax Call Failed')
		}
	});
});

