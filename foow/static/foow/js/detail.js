$(function(){
	if($('#headerText').text() == 'Weihnachtsmärkte')
	{
		$('#headerText').text() = 'Weihnachts-märkte';
	}
	if($('#nextID').length){
		var nextID = $('#nextID').html();
		$('.next').find('a').attr('href','/post/'+nextID)
	}
	else
	{
		$('.next').hide();
	}

	if($('#previousID').length){
		var prevID = $('#previousID').html();
		$('.previous').find('a').attr('href','/post/'+prevID)
	}
	else{
		$('.previous').hide();
	}
});