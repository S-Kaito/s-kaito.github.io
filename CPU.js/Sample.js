var arg = new Object;
var pair=location.search.substring(1).split('&');
for(var i=0;pair[i];i++) {
    var kv = pair[i].split('=');
    arg[kv[0]]=kv[1];
}

function init(){
	
	if(arg.id=="0"){
		theme = new Slide(TYPE.TITLE);
		theme.setTitle("自作CPUの紹介");
	
		theme.addSentence(0,"ソフトウェア情報学部ソフトウェア情報学科");
		theme.addSentence(0,"小山 海渡");
		theme.show();
	
		document.onkeydown = function(e){
			if(e.keyCode == 39)
				window.location.href = window.location.pathname + "?id=1";
		}
	}else if(arg.id=="1"){
		theme = new Slide(TYPE.CONTENTS);
		theme.setTitle("自己紹介");
	
		theme.addSentence(0,"・基本情報")
		theme.addSentence(1,"・氏名：小山 海渡");
		theme.addSentence(1,"・所属：ソフトウェア情報学部 M1");
		theme.addSentence(1,"            社会情報システム学講座(阿部研)");
		theme.addSentence(0,"");

		theme.show();
		document.onkeydown = function(e){
			if(e.keyCode == 39)
				window.location.href = window.location.pathname + "?id=2";
			if(e.keyCode == 37)
				window.location.href = window.location.pathname + "?id=0";
		}
	}else if(arg.id=="2"){
		theme = new Slide(TYPE.CONTENTS);
		theme.setTitle("自己紹介");
	
		theme.addSentence(0,"・基本情報")
		theme.addSentence(1,"・氏名：小山 海渡");
		theme.addSentence(1,"・所属：ソフトウェア情報学部 M1");
		theme.addSentence(1,"            社会情報システム学講座(阿部研)");
		theme.addSentence(0,"");
		theme.addSentence(0,"・最近の流行り");
		theme.addSentence(1,"・Identity V");
		theme.addSentence(1,"・MOBA");
		theme.addSentence(1,"・JavaScript");
		theme.addSentence(1,"・Python");

		theme.show();
		document.onkeydown = function(e){
			if(e.keyCode == 39)
				window.location.href = window.location.pathname + "?id=3";
			if(e.keyCode == 37)
				window.location.href = window.location.pathname + "?id=1";
		}
	}
}



