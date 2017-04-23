$(function(){
	var arrayOfIds = $.map($(".galleryImages"), function(n, i){
  		return n.id;
	});
	//alert(arrayOfIds);
	$('.galleryImages').each(function(){
		$(this).click(function(){
			var imgID = this.id.substr(3);
			loadModal(imgID, arrayOfIds);
		});
		
	});
});

function loadModal(imgID, arrayOfIds){
	$.ajax({
		type: 'GET',
		url: "/picture/"+imgID,
		datatype: 'json',
		success: function(data){
			$.each(data, function(index, element){
				var picture = '/media/'+element.fields.picture;
				var description = element.fields.picture_description;
				var nextID = getNext(imgID, arrayOfIds);
				var previousID = getPrevious(imgID, arrayOfIds);
				//alert(nextID);
				//alert(previousID);

				if(nextID == null){
					$('#nextPic').hide();
				}
				else{
					$('#nextPic').show();
					$('#nextPic').unbind( "click" );
					$('#nextPic').click(function(){
						loadModal(nextID.substr(3), arrayOfIds);
					});
				}
				if(previousID == null){
					$('#previousPic').hide();
				}
				else{
					$('#previousPic').show();
					$('#previousPic').unbind( "click" );
					$('#previousPic').click(function(){
						loadModal(previousID.substr(3), arrayOfIds);
					});
				}

				$('#modalImage').attr('src', picture);
				$('#modalText').html(description);
				$('#picModal').modal();


			});
		}
	});
}

function getNext(imgID, arrayOfIds){
	for(var i=0; i < arrayOfIds.length; i++){
		//alert(arrayOfIds[i]);
		if(arrayOfIds[i] == 'img'+imgID)
		{
			if(arrayOfIds.length > i + 1)
				return arrayOfIds[i + 1];
		}
	}
	return null;
}

function getPrevious(imgID, arrayOfIds){
	for(var i=0; i < arrayOfIds.length; i++){
		if(arrayOfIds[i] == 'img'+imgID)
		{
			if(i != 0)
				return arrayOfIds[i - 1];
		}
	}
	return null;
}
