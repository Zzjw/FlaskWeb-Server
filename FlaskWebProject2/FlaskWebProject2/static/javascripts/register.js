register = function () {
    //alert("!!!");
    // if($("#user").val()==""){
    // 	alert("请输入用户名");
    // 	return false;
    // }
    // if($("#password").val()==""){
    // 	alert("请输入密码");
    // 	return false;
    // }
    // if($("#email").val()==""){
    // 	alert("请输入邮箱");
    // 	return false;
    // }
    $.ajax({
        type: 'POST',
        url: '/register_check',
        data: JSON.stringify({
            username: $("#username").val(),
            password: $("#password").val(),
            confirm: $("#confirm").val(),
            email: $("#email").val()
        }),
        contentType: 'application/json; charset=UTF-8',
        success: function (data) {
            if (data == 'succeed') {
                alert("注册成功");
                window.location.href="/login";
                return false;
            }
            else if (data == 'username-error') {
                alert("The username has been registered, please select another one.");
                //$("#username").focus();
                return false;
            }
            else if (data == 'username-length-error') {
                alert('Your username should be made up of 3~20 lowercase letters or digits, and begin with a letter.')
                return false;
            }
            else if (data == 'password-is-null') {
                alert('The passwords can\'t be null');
            }
            else if (data == 'password_diff') {
                alert('Your passwords do not match.');
                return false;
            }
            else if (data = 'email-error') {
                alert("The mailbox format is incorrect");
                return false;
            }
        }
    })
}