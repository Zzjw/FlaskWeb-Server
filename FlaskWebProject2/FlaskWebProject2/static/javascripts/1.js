// join    split


window.onload=function(){
	
	var x=GetRequest();
	//var jpg=document.getElementById(0);
	var jpg=$('#0')[0];
	//if(jpg)	jpg.src=x;
	var div_example=document.getElementById("example");
	//sdiv_example=$(example);
	/*document.getElementById("changebutton").onclick=function(){
		div_example.textContent="<p>新文本内容</p>"
	}*/
	changeTextContent=function(){
		div_example.textContent="<p>新文本内容</p>"
	}
	changeInnerHTML=function(){
		div_example.innerHTML="<p>新文本内容</p>"
	}
}

function GetRequest() {
    var url = location.search; //获取url中"?"符后的字串
    var theRequest = new Object();
    if (url.indexOf("?") != -1) {
        var str = url.substr(1);
        strs = str.split("&");
        for (var i = 0; i < strs.length; i++) {
            theRequest[strs[i].split("=")[0]] = decodeURIComponent(strs[i].split("=")[1]);
        	}
	    }
	    return "images/"+theRequest.user+".jpg";
	}