# Emissions-Graph-Generator-Microservice

## MIcroservice developed for CS 361 - Group 80.  Utilizes a REST API built with Python and Flask.

The program receives a GET request containg the parameters of a valid location and time frame, generates a graph with MatPlotLib to display that data, then responds to the request sending the graph back to the Web UI client.  

### Request Data:
Data is requested by assigning a URL endpoint to "http://localhost8080/api/graph".  The client then collects a payload of location and timeframe through the clients UI and sends a http GET request to the URL endpoint with the payload attached as parameters (Location=string/char, TimeFrame=List/Array).   

### Receive Data:
Once the data is requested the graph is generated and sent back as a response.  Depending on implementation you can access the URL of the response to view the graph by itself or you can uncomment the route that generates a template HTML response containing the graph.  Currenlty the response is generated utilizing the FLask make_response object with the content of the object set to the graph. 

### UML DIagram: 
![UML Diagram](images/UML.png)

### Communication Agreement:
![Group Communication Protocol](images/group80.png)