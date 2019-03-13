var express = require('express')
var ejs = require('ejs')

var app = express()

app.engine('ejs',ejs.renderFile)

app.get('/',(req,res) =>{
	res.render("index.ejs",{title: "Hello,world!" , content: "Hello,node.js with express!" });
})
var server = app.listen(3000,()=>{
	console.log('Start')
})