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

// function authenticate() {
//   return gapi.auth2.getAuthInstance()
//       .signIn({scope: "https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.readonly https://www.googleapis.com/auth/spreadsheets https://www.googleapis.com/auth/spreadsheets.readonly"})
//       .then(function() { console.log("Sign-in successful"); },
//             function(err) { console.error("Error signing in", err); });
// }
// function loadClient() {
//   gapi.client.setApiKey("YOUR_API_KEY");
//   return gapi.client.load("https://content.googleapis.com/discovery/v1/apis/sheets/v4/rest")
//       .then(function() { console.log("GAPI client loaded for API"); },
//             function(err) { console.error("Error loading GAPI client for API", err); });
// }
// // Make sure the client is loaded and sign-in is complete before calling this method.
// function execute() {
//   return gapi.client.sheets.spreadsheets.get({
//     "spreadsheetId": "1LTyngHx8IoXXXzzqyOdR8joznYvqsHa445BZCzmvGho",
//     "includeGridData": true,
//     "ranges": [
//       "入力一覧!A:D"
//     ]
//   })
//       .then(function(response) {
//               // Handle the results here (response.result has the parsed body).
//               console.log("Response", response);
//             },
//             function(err) { console.error("Execute error", err); });
// }

// gapi.load("client:auth2", function() {
//   gapi.auth2.init({client_id: "AIzaSyDsALLGV073QfMilPkwsUJfAMrKFI8VWDE"});
// });

// //authenticate().then(loadClient)
// var data = execute()

// console.log(data.properties.title)

// data.sheets[0].data.forEach(d=>{
//   d.forEach(rowData =>{
//     rowData.forEach(values =>{
//       console.log(value.formattedValue)
//     })
//   })
// })