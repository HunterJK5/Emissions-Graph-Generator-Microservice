import requests
import webbrowser
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO

# sets api endpoint to connect to.  If you change the port num be sure to change here as well
url = "http://localhost:8080/api/graph"

generate = True

while generate:
    # simple CLI UI to gather data parameters to be requested
    country = input("Please Enter the Counrty to view Emissions data for: ")
    start_date = int(input("Please Enter the Starting Year for your Time Period: "))
    end_date = int(input("Please Enter the Ending Year for your Time Period: "))

    time_period = []

# fill time period parameter with all years in the selected period
    while start_date <= end_date:
        time_period.append(str(start_date))
        start_date += 1

# payload parameters that will be sent in the request
    payload = {"Country": country, "TimePeriod": time_period}

# send GET request to the Server
    response = requests.get(url, params=payload)


# microservice has been implemented to send to web UI.
# For assignment purposes I am launching the url recived in the response.
# You can change the template in how the data is viewed in a web UI
    webbrowser.open(response.url)

# Load graph from response content
    im = Image.open(BytesIO(response.content))
    plt.imshow(im)
    plt.show()

    new = input("Generate a new graph? [Y/N] ")

    if new == "N":
        generate = False

