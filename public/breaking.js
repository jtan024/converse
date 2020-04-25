var url = 'http://newsapi.org/v2/top-headlines?' +
    'country=us&' +
    'apiKey=API_KEY';
var req = new Request(url);
fetch(req)
    .then(function(response) {
        console.log(response.json());
    })