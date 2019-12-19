Airports
---------


## Endpoints

**`/iata/<code>`**

- Returns a JSON response for 1 airport. 
- Allows case insensitive searching. ("sxf" should find "SXF") 
- Returns the appropriate HTTP code on errors.

**`/airports`**

- Returns a JSON response with all airports. 
- With the parameter `name=<name>` returns a JSON response with a list of matching airports.
- Allows case insensitive searching and partial matches.
- Returns the appropriate HTTP code on errors (however, [an empty list is not an error](https://softwareengineering.stackexchange.com/a/358245)).


## Run the app

    pip install -r requirements.txt
    flask run


## Test the app

With your favorite testing framework. E.g. from the command line:

    ➜  ~ curl http://127.0.0.1:5000/iata/TXL
    {"city":"Berlin","country":"Germany","iata":"TXL","icao":"EDDT","latitude":52.5597,"longitude":13.2877,"name":"Berlin-Tegel Airport"}

    ➜  ~ curl http://127.0.0.1:5000/airports?name=tegel
    [{"city":"Berlin","country":"Germany","iata":"TXL","icao":"EDDT","latitude":52.5597,"longitude":13.2877,"name":"Berlin-Tegel Airport"}]

    ➜  ~ curl http://127.0.0.1:5000/iata/TXX
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>