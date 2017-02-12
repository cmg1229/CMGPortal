$(function(){
	$('.galleryImages').each(function(){
		$(this).click(function(){
			var imgID = this.id.substr(3);
			$.ajax({
				type: 'GET',
				url: "/picture/"+imgID,
				datatype: 'json',
				success: function(data){
					$.each(data, function(index, element){
						var picture = '/media/'+element.fields.picture;
						var description = element.fields.picture_description;
						$('#modalImage').attr('src', picture);
						$('#modalText').html(description);
						$('#picModal').modal();
					});
				}
			});
		});
		
	});
});