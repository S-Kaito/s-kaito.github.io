const http = require('http');
const fs   = require('fs');
const ejs  = require('ejs');
const url  = require('url');
const qs   = require('querystring');

const pageIndex = fs.readFileSync('node.ejs','utf8');
const style = fs.readFileSync('style.css','utf8');

function main(){
	var server = http.createServer(getFromClient);
	server.on("request",onStart);
	server.listen(3000);
	console.log('Start!');
}

function getFromClient(request,response){
	switch(url.parse(request.url).pathname){
		case '/':
			var content = ejs.render(pageIndex,{
				title:"Hello,Node.js!",
				content:"Welcome to Node.js world!",
				rasberry: "<img src=\"rasberry01.png\" alt=\"rasberry.py\">"
			});
			
			response.writeHead(200,{'Content-Type':'text/html'});
			response.write(content);
			response.end();
			
			break;
		case '/style.css':
			response.writeHead(200,{'Content-Type':'text/css'});
			response.write(style);
			response.end();
			break;
	}
}
function onStart(request,response){
	if(request.method=="POST"){
		data = "";
		request.on("data",function(d){
			data += d
		})
		request.on("end",function(){
			var query = qs.parse(data);
			console.log(query);
			var content = ejs.render(pageIndex,{
				title:"Hello,Node.js!",
				content:"Welcome to Node.js world!",
				rasberry: "<img src=\"" + (query.volt > 0.5 ? "rasberry01.png" : "rasberry02.png") + "\" alt=\"rasberry.py\">"
			});
			response.writeHead(200, {'Content-Type' : 'text/html'});
			response.write(content);
			response.end();
		})
		
	}	
}
main();