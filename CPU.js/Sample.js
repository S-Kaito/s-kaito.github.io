var arg = new Object;
var pair=location.search.substring(1).split('&');
for(var i=0;pair[i];i++) {
    var kv = pair[i].split('=');
    arg[kv[0]]=parseFloat(kv[1]);
}

function init(){
	if(arg.id=="0" || arg.id==null){
		theme = new SlideDark(TYPE.TITLE);
		theme.setTitle("自作CPUの紹介");
	
		theme.addSentence(0,"ソフトウェア情報学部ソフトウェア情報学科");
		theme.addSentence(0,"小山 海渡");
		theme.setOnNext(function(e){
			window.location.href = window.location.pathname + "?id=1";
		});
		theme.show();

		// document.onkeydown = function(e){
		// 	if(e.keyCode == 39)
		// 		window.location.href = window.location.pathname + "?id=1";
		// }
		// document.ontouchstart = function(e){
		// 	if(changedTouches[0].pageX > width / 2)
		// 		window.location.href = window.location.pathname + "?id=1";
		// }
	}
	if(arg.id=="1"){
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("自己紹介");
	
		theme.addSentence(0,"・基本情報")
		theme.addSentence(1,"・氏名：小山 海渡");
		theme.addSentence(1,"・所属：ソフトウェア情報学部 M1");
		theme.addSentence(1,"            社会情報システム学講座");
		theme.addSentence(0,"");
		theme.setOnNext(function(e){
			window.location.href = window.location.pathname + "?id=2";
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=0";
		});
		theme.show();
		
	}else if(arg.id=="2"){
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("自己紹介");
	
		theme.addSentence(0,"・基本情報")
		theme.addSentence(1,"・氏名：小山 海渡");
		theme.addSentence(1,"・所属：ソフトウェア情報学部 M1");
		theme.addSentence(1,"            社会情報システム学講座");
		theme.addSentence(0,"");
		theme.addSentence(0,"・最近の流行り");
		theme.addSentence(1,"・Identity V");
		theme.addSentence(1,"・MOBA");
		theme.addSentence(1,"・JavaScript");
		theme.addSentence(1,"・Python");
		theme.setOnNext(function(e){
			window.location.href = window.location.pathname + "?id=3";
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=1";
		});
		theme.show();
		
	}else if(arg.id=="3"){
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("CPUとは");
	
		theme.br(4);
		theme.addSentence(0,"C");
		theme.addSentence(0,"P");
		theme.addSentence(0,"U");
		theme.setOnNext(function(e){
			window.location.href = window.location.pathname + "?id=4";
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=2";
		});
		theme.show();
	}else if(arg.id=="4"){
		let count = 0;
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("CPUとは");

		theme.br(4);
		theme.addSentence(0,"Central ");
		theme.addSentence(0,"Processing ");
		theme.addSentence(0,"Unit");
		theme.setOnNext(function(e){
			if(count == 0){
				theme.addSentence(0,"");
				theme.addSentence(0,"ではなく！！");
				count++;
				theme.show();
			}else if(count == 1){
				window.location.href = window.location.pathname + "?id=5";
}
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=3";
		});
		theme.show();

	}else if(arg.id=="5"){
		let count = 0;
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("CPUとは");
	

		theme.addSentence(0,"");
		theme.addSentence(0,"");
		theme.addSentence(0,"");
		theme.addSentence(0,"");

		theme.addSentence(0,"Canvas ");
		theme.addSentence(0,"Presentation ");
		theme.addSentence(0,"Unit");
		theme.setOnNext(function(e){
			if(count == 0){
				theme.addSentence(0,"");
				theme.addSentence(1,"Webサイトでプレゼンテーション");
				theme.addSentence(1,"をするライブラリ");
				count++;
				theme.show();
		
			}else if(count == 1){
				window.location.href = window.location.pathname + "?id=5.5";
			}
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=4";
		});
		theme.show();
	}else if(arg.id=="5.5"){
		let count = 0;
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("実践編");
	
		theme.br(4);
		theme.setOnNext(function(e){
			if(count == 0){
				theme.addSentence(0,"今から実演します！！");
			}else if(count == 1){
				theme.br(1);
				theme.addSentence(0,"アレ・・・・・？");
			}else if(count == 2){
				theme.br(2);
				theme.addSentence(0,"(°∀°)ｱﾋｬﾋｬﾋｬﾋｬﾋｬﾋｬﾋｬﾋｬﾋｬﾋ");
			}else{
				window.location.href = window.location.pathname + "?id=6";
			}
			count++;
			theme.show();
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=5";
		});
		theme.show();
	}else if(arg.id=="6"){
		let count = 0;
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("CPUのメリット①");
		
		theme.addSentence(0,"マウスが必要ない！");
		theme.addSentence(1,"キーボードのみで実装可");
		theme.addSentence(1,"PowerPointも不要");
		theme.addSentence(1,"メモ帳で実装可能！");
		theme.setOnNext(function(e){
			if(count==0){
				theme.addSentence(0,"");
				theme.addSentence(0,"　↓");
				theme.addSentence(0,"");
				theme.addSentence(0,"準備がメッチャ楽！");
				theme.show();
				count++;
			}else if(count == 1){
				window.location.href = window.location.pathname + "?id=7";
			}
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=5.5";
		});
		theme.show();
	}else if(arg.id=="7"){
		let count = 0;
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("CPUのメリット②");
		
		theme.addSentence(0,"JSの恩恵を受けられる");
		theme.setOnNext(function(e){
			if(count==0)
				theme.addSentence(1,"node.js");
			if(count==1)
				theme.addSentence(1,"TensowFlow.js");
			if(count==2)
				theme.addSentence(1,"ApexChart.js");
			if(count==3){
				theme.addSentence(0,"");
				theme.addSentence(0,"    |");
				theme.addSentence(0,"    |");
				theme.addSentence(0,"    |");
				theme.addSentence(0,"    V");
				theme.addSentence(0,"より高度なプレゼンが可能！！");
			}
			if(count==4)
				window.location.href = window.location.pathname + "?id=8";
			theme.show();
			count++;
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=8";
		});
		theme.show();
	}else if(arg.id=="8"){
		let count = 0;
		let width = window.parent.screen.width;
		let height = window.parent.screen.height;
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("CPUのメリット③");
		
		theme.setOnNext(function(e){
			window.location.href = window.location.pathname + "?id=9";
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=7";
		});
		theme.show();
		
		var img = new Image();
		img.src = "QRCode01.png";
		img.onload = function(){
			console.log("aaa");
			if(width > 500)
				theme.ctx.drawImage(img,width / 7 * 4,height / 9,width / 3,width / 3);
			else
				theme.ctx.drawImage(img,width / 5,70);
		}

	}else if(arg.id=="8.5"){
		let count = 0;
		theme = new SlideDark(TYPE.CONTENTS);
		theme.setTitle("CPUのメリット③");
		theme.br(4);
		theme.addSentence(0,"レスポンシブウェブデザインが可能！！");
		theme.setOnNext(function(e){
			window.location.href = window.location.pathname + "?id=9";
		});
		theme.setOnPrevious(function(e){
			window.location.href = window.location.pathname + "?id=8";
		});
		theme.show();
	}
}