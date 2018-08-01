
var TYPE = {
	TITLE : 0,
	SUB_TITLE : 1,
	CONTENTS : 2,
	SUMMARY : 9
}
class Controller{
	constructor(){
		this.slides = new Array();
		this.id = -1;
		this.count = 0;
	}
	addSlide(slide){
		this.slides.append(slide);
	}
	next(){
		this.id += 1;
		this.count = 0;
		this.slides[id].show();
	}
	onKeyDown(e){
		this.slides[id].onKeyDown();
	}
}
class Slide{
	constructor(type){
		this.canvas = null;
		this.title="";
		this.sentence = new Array();
		this.level = new Array();
		this.type = type;
		this.onKeyDown = null;
	}
	setTitle(title){
		this.title = title;
	}
	setOnKeyDown(func){
		this.onKeyDown = func;
	}
	addSentence(level,sentence){
		this.level.push(level);
		this.sentence.push(sentence);
	}
	clearSentence(){
		this.level = new Array();
		this.sentence = new Array();
	}
	br(){
		br(1);
	}
	br(count){
		for(i = 0;i < count;i++)
			addSentence(0,"");
	}
	show(){
		console.log("CPUException : show() is not override");
	}
}
class SlideDark extends Slide{
	constructor(type){
		super(type);
		this.backgroundColor = "#FFFFFF";
		this.mainColor = "#31394d";
		this.accentColor = "#FF0000";
	}
	show(){
		let form = document.body;
		form.style.overflow = "hidden";
		form.style.margin = "0px 0px 0px 0px";
		
		var width = window.parent.screen.width;
		var height = window.parent.screen.height;
		console.log(width + " " + height);
		form.innerHTML = "<canvas id=\"background\" width=\"" + width + "\" height=\"" + height + "\"" + "></canvas>";
		var ctx = document.getElementById('background').getContext('2d');
		if(width > 499){
			if(this.type==TYPE.TITLE){
				ctx.fillStyle = this.backgroundColor;
				ctx.fillRect(0,0,width,height);
				ctx.beginPath();
				ctx.fillStyle = this.mainColor;
				ctx.moveTo(0,height / 8 * 5);
				ctx.lineTo(0,height);
				ctx.lineTo(width,height);
				ctx.lineTo(width,height / 8 * 3);
				ctx.fill();

				ctx.textAlign = "left";
				ctx.font = "70px 'ＭＳ Ｐゴシック'";
				ctx.fillStyle = this.mainColor;
				ctx.fillText(this.title,50,100);

				ctx.textAlign = "right";
				ctx.font = "40px 'ＭＳ Ｐ明朝体'";
				ctx.fillStyle = this.backgroundColor;
				for(i = 0;i < this.sentence.length;i++){
					ctx.fillText(this.sentence[i],width - 50,height - 150 + i * 40);
				}
			}else if(this.type == TYPE.SUB_TITLE){
				ctx.fillStyle = this.backgroundColor;
				ctx.fillRect(0,0,width,height);
				ctx.fillStyle = this.mainColor;
				ctx.fillRect(0,height - 40,width,height);
				
				ctx.textAlign = "left";
				ctx.font = "70px 'ＭＳ Ｐゴシック'";
				ctx.fillStyle = this.mainColor;
				ctx.fillText(this.title,50,height / 2);

				ctx.font = "40px 'ＭＳ Ｐ明朝体'";
				ctx.fillStyle = this.backgroundColor;
				for(i = 0;i < this.sentence.length;i++){
					ctx.fillText(this.sentence[i],50 + 50 * this.level[i],height / 2 + 70 + i * 40);
				}
			}else if(this.type == TYPE.CONTENTS){
				ctx.fillStyle = this.backgroundColor;
				ctx.fillRect(0,0,width,height);
				ctx.fillStyle = this.mainColor;
				ctx.fillRect(0,0,width / 20 * 9,height);
				
				ctx.strokeStyle = this.backgroundColor;
				ctx.lineWidth = 3;
				ctx.beginPath();
				ctx.moveTo(0,height / 8 * 5);
				ctx.lineTo(width / 2,height / 2);
				ctx.closePath();
				ctx.stroke();

				ctx.textAlign = "left";
				ctx.font = "70px 'ＭＳ Ｐゴシック'";
				ctx.fillStyle = this.backgroundColor;
				ctx.fillText(this.title,20,80);
				
				ctx.fillStyle = this.mainColor;
				for(i = 0;i < this.sentence.length;i++){
					ctx.font = (45 - 10 * this.level[i]) + "px 'ＭＳ Ｐ明朝体'";
					ctx.fillText(this.sentence[i],width / 2 + 10 + 50 * this.level[i],100 + i * 50);
				}
			}else if(this.type == TYPE.SUMMARY){
				
			}
		}else{
			if(this.type==TYPE.TITLE){
				ctx.fillStyle = this.backgroundColor;
				ctx.fillRect(0,0,width,height);
				ctx.beginPath();
				ctx.fillStyle = this.mainColor;
				ctx.moveTo(0,height / 8 * 5);
				ctx.lineTo(0,height);
				ctx.lineTo(width,height);
				ctx.lineTo(width,height / 8 * 3);
				ctx.fill();

				ctx.textAlign = "left";
				ctx.font = "30px 'ＭＳ Ｐゴシック'";
				ctx.fillStyle = this.mainColor;
				ctx.fillText(this.title,20,40);

				ctx.textAlign = "right";
				ctx.font = "15px 'ＭＳ Ｐ明朝体'";
				ctx.fillStyle = this.backgroundColor;
				for(i = 0;i < this.sentence.length;i++){
					ctx.fillText(this.sentence[i],width - 20,height - 50 + i * 20);
				}
			}else if(this.type == TYPE.SUB_TITLE){
				ctx.fillStyle = this.backgroundColor;
				ctx.fillRect(0,0,width,height);
				ctx.fillStyle = this.mainColor;
				ctx.fillRect(0,height - 40,width,height);
				
				ctx.textAlign = "left";
				ctx.font = "70px 'ＭＳ Ｐゴシック'";
				ctx.fillStyle = this.mainColor;
				ctx.fillText(this.title,50,height / 2);

				ctx.font = "40px 'ＭＳ Ｐ明朝体'";
				ctx.fillStyle = this.backgroundColor;
				for(i = 0;i < this.sentence.length;i++){
					ctx.fillText(this.sentence[i],50 + 50 * this.level[i],height / 2 + 70 + i * 40);
				}
			}else if(this.type == TYPE.CONTENTS){
				ctx.fillStyle = this.backgroundColor;
				ctx.fillRect(0,0,width,height);
				ctx.fillStyle = this.mainColor;
				ctx.fillRect(0,0,width / 6,height);
				
				ctx.strokeStyle = this.backgroundColor;
				ctx.lineWidth = 3;
				ctx.beginPath();
				ctx.moveTo(0,height / 8 * 5);
				ctx.lineTo(width / 6,height / 2);
				ctx.closePath();
				ctx.stroke();

				ctx.textAlign = "left";
				ctx.font = "30px 'ＭＳ Ｐゴシック'";
				ctx.fillStyle = this.mainColor;
				ctx.fillText(this.title,width / 6 + 10,30);
				
				ctx.fillStyle = this.mainColor;
				for(i = 0;i < this.sentence.length;i++){
					ctx.font = (20 - 7 * this.level[i]) + "px 'ＭＳ Ｐ明朝体'";
					ctx.fillText(this.sentence[i],width / 6 + 17 * this.level[i],100 + i * 20);
				}
			}else if(this.type == TYPE.SUMMARY){
				
			}
		}
	}
}
