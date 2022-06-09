function get_weather(){

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '37c02cdfd6mshdf3008d2ab53768p188854jsna994e5734add',
		'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
	}
};

fetch('https://weatherapi-com.p.rapidapi.com/current.json?q=Lisbon', options)
	.then(response => response.json())
	.then
	(data =>
	    {
        const weather = data;
        document.getElementById('weather').innerHTML = String(weather.location.name)+ ": " + String(weather.current.condition.text);
        document.getElementById('temperature').innerHTML = "Temperature: " + String(weather.current.temp_c) + "ºC";
        document.getElementById('wind').innerHTML = "Wind: " + String(weather.current.wind_kph) + " Kmh";
        document.getElementById('humidity').innerHTML = "Humidity Level: " + String(weather.current.humidity);
        }
    );
}


function get_random_joke(){

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '37c02cdfd6mshdf3008d2ab53768p188854jsna994e5734add',
		'X-RapidAPI-Host': 'dad-jokes.p.rapidapi.com'
	}
};

fetch('https://dad-jokes.p.rapidapi.com/random/joke', options)
	.then(response => response.json())
  //.then(response => console.log(response))
	.then
	(data =>
	    {
	     const joke = data;
       console.log(data.body[0].setup)
	     document.getElementById('setup').innerHTML = String(data.body[0].setup);
        document.getElementById('punchline').innerHTML = String(data.body[0].punchline);
	    }

	);

}