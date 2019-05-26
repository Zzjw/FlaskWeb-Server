Login=function(){
	if(window.event.keyCode==13){
		login();
	}
}
login=function(){
	$.ajax({
		type:'POST',
		url:'/login_check',
		data:JSON.stringify({
            username: $("#username").val(),
            password: $("#password").val()
		}),
        contentType: 'application/json; charset=UTF-8',
		success:function(data){
			if(data=='succeed'){
				//alert("注册成功");
				window.location.href="/home";
				return true;
			}
			else if(data=='no_such_user'){
				alert("No such user!");
			}
			else if(data=='password_wrong'){
				alert("Password wrong!");
                $("#password").focus();
			}
		}
	})
}
