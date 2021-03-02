const nodeTitle = document.getElementsByClassName("title")[0];
nodeTitle.insertAdjacentHTML('beforebegin', `
	<img class="icon" src="pic/link.png" onclick="onClickLink(this)"/>
	<img class="icon" src="pic/twitter.png" onclick="onClickTweet()"/><br>
`);

function onClickLink(e){
	navigator.clipboard.writeText(location.href);
	alert("クリップボードにURLをコピーしました");
}

function onClickTweet(e){
	window.location.href = `https://twitter.com/intent/tweet?&text=${document.title}&url=${location.href}`;
}