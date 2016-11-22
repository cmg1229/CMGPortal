function emailTest(){
	var emailtest = /^[-a-z0-9~!$%^&*_=+}{\'?]+(\.[-a-z0-9~!$%^&*_=+}{\'?]+)*@([a-z0-9_][-a-z0-9_]*(\.[-a-z0-9_]+[a-z][a-z])|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,5})?$/i;
	var email = $('#email').val();
	if(!emailtest.test(email))
	{
		alert('Must Enter a valid email address!');
		return false;
	}
	else
	{
		return true;
	}
}
