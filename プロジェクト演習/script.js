var options = {
	chart: {
		type: 'line'
	},
	series: [{
		name: 'templature',
		data:       [24, 22, 21, 21, 21, 20, 20, 20, 20, 20, 20, 19, 19, 19, 18, 22, 22, 23, 23, 23, 23, 23, 22, 20, 19, 18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 17]
	}],
	xaxis: {
		categories: [01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
	}
}

var chart = new ApexCharts(document.querySelector("#chart"),options);
chart.render();

var URL = "https://asia-northeast1-sheetstowebapi.cloudfunctions.net/api?id=1kYpww4GAVxaIJINnly1WAPiW7FGOK87qptPIA_9mtAA&range=%E5%85%A5%E5%8A%9B%E4%B8%80%E8%A6%A7!A1:AC1033"


// fetch(URL).then(function (data) {
// 	return data.json();
// }).then(function (json) {
// 	json.forEach(data =>{
// 		document.getElementById('sheet-data').insertAdjacentHTML("afterbegin",`
// 			<tr>
// 				<td>` + data["タイムスタンプ"] + `</td>
// 				<td>` + data["鶏舎番号"] + `</td>
// 				<td>` + data["死亡羽数"] + `</td>
// 				<td>` + data["生産個数"] + `</td>
// 				<td>` + data["生産量"] + `</td>
// 				<td>` + data["飼料採食量"] + `</td>
// 				<td>` + data["規格外卵量"] + `</td>
// 			</tr>
// 		`);
// 	})
// });

var xhr = new XMLHttpRequest();

// ハンドラの登録.
xhr.onreadystatechange = function() {
	switch ( xhr.readyState ) {
		case 0:
			// 未初期化状態.
			console.log( 'uninitialized!' );
			break;
		case 1: // データ送信中.
			console.log( 'loading...' );
			break;
		case 2: // 応答待ち.
			console.log( 'loaded.' );
			break;
		case 3: // データ受信中.
			console.log( 'interactive... '+xhr.responseText.length+' bytes.' );
			break;
		case 4: // データ受信完了.
			var json = xhr.responseText;
			console.log( 'COMPLETE! :'+ json );
			json.forEach(data =>{
				document.getElementById('sheet-data').insertAdjacentHTML("afterbegin",`
					<tr>
						<td>` + data["タイムスタンプ"] + `</td>
						<td>` + data["鶏舎番号"] + `</td>
						<td>` + data["死亡羽数"] + `</td>
						<td>` + data["生産個数"] + `</td>
						<td>` + data["生産量"] + `</td>
						<td>` + data["飼料採食量"] + `</td>
						<td>` + data["規格外卵量"] + `</td>
					</tr>
				`);
			})
			break;
	}
};

xhr.open( 'POST', URL, true );
xhr.setRequestHeader( 'Content-Type', 'application/x-www-form-urlencoded' );
xhr.send();

var MY_API_KEY = "AIzaSyD__zlsHpxJftnf3XPbesS0Vg6dkEsemvE"
var MY_CLIENT_ID = "32829900074-t5q3ei0qb7dug362m9ajrv20k0hr286k.apps.googleusercontent.com"
var MY_CLIENT_SECLET = "HuFAj5QWTs6wjeIsRCx7LzeI"

// var API = "AIzaSyDsALLGV073QfMilPkwsUJfAMrKFI8VWDE"
// var CLIENT = "1LTyngHx8IoXXXzzqyOdR8joznYvqsHa445BZCzmvGho"

// function authenticate() {
// 	return gapi.auth2.getAuthInstance()
// 		.signIn({scope: "https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.readonly https://www.googleapis.com/auth/spreadsheets https://www.googleapis.com/auth/spreadsheets.readonly"})
// 		.then(function() { 
// 			console.log("Sign-in successful"); 
// 		},function(err) { 
// 			console.error("Error signing in", err); 
// 		});
// }
// function loadClient() {
// 	gapi.client.setApiKey(API);
// 	return gapi.client.load("https://content.googleapis.com/discovery/v1/apis/sheets/v4/rest")
// 	.then(function() { 
// 		console.log("GAPI client loaded for API"); 
// 	},function(err) { 
// 		console.error("Error loading GAPI client for API", err); 
// 	});
// }
// // Make sure the client is loaded and sign-in is complete before calling this method.
// function execute() {
// 	return gapi.client.sheets.spreadsheets.get({
// 		"spreadsheetId": CLIENT,
// 		"includeGridData": true,
// 		"ranges": [
// 			"入力一覧!A:D"
// 		]
// 	}).then(function(response) {
// 		// Handle the results here (response.result has the parsed body).
// 		console.log("Response", response);
// 	},function(err) { 
// 			console.error("Execute error", err);
// 	});
// 	//authenticate().then(loadClient)

// 	console.log(data.properties.title)

// 	data.sheets[0].data.forEach(d=>{
// 		d.forEach(rowData =>{
// 			rowData.forEach(values =>{
// 				console.log(value.formattedValue)
// 			})
// 		})
// 	})
// }

// gapi.load("client:auth2", function() {
// 	gapi.auth2.init({client_id: CLIENT});
// });