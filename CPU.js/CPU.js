
var TYPE = {
	TITLE : 0,
	SUB_TITLE : 1,
	CONTENTS : 2,
	SUMMARY : 9
}
class Slide{
	constructor(type){
		this.canvas = null;
		this.title="";
		this.sentence = new Array();
		this.level = new Array();
		this.type = type;
	}
	setTitle(title){
		this.title = title;
	}
	addSentence(level,sentence){
		this.level.push(level);
		this.sentence.push(sentence);
	}
	clearSentence(){
		this.level = new Array();
		this.sentence = new Array();
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
		
		var width = screen.width;
		var height = screen.height;
		
		form.innerHTML = "<canvas id=\"background\" width=\"" + width + "\" height=\"" + height + "\"" + "></canvas>";
		var ctx = document.getElementById('background').getContext('2d');

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

	}
}
