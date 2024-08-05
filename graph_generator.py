from flask import Flask, request, make_response, render_template
import matplotlib.pyplot as plt
import numpy as np
import io
import json


app = Flask(__name__)

@app.route("/api/graph", methods=["GET"])
def generate_graph(): 

# Fetch the location and time frame sent through the GET request
    location = request.args.get("Country")
    time_period = request.args.getlist("TimePeriod")

# open data to parse
    file = open('data/GCB_percapita.json')   # change location if you plan to store data elsewhere
    data = json.load(file)

# initialize lists to store the data that will be graphed
    data_x = []
    data_y = []

# parse through json data to fetch requested data.  Loop will end at EOF or when all requested data has been found
    for entry in data:
        if entry["Country"] == location and entry["Year"] in time_period:
            year = int(entry["Year"])
            emissions = float(entry["Total"])
            data_x.append(year)
            data_y.append(emissions)
            time_period.remove(str(year))       # remove year to track when all data is found
        if not time_period:
            # all data has been found so loop can exit early
            break
    
    # store data to be graphed
    xpoints = np.array(data_x)
    ypoints = np.array(data_y)

# plot the data arrays in the graph and label axis
    plt.plot(xpoints, ypoints)
    plt.xlabel("Time Period")
    plt.ylabel("Total Emissions")

# save graph as png and store as byte value so that the data can be sent to the html template
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

# send http response with byte value of the image so image can be displayed in the html template 
    response = make_response(buf.getvalue())
    response.mimetype = "image/png"

# close json file
    file.close()

    return response

"""This route is designed to display the returned graph in a html template stored in this repo.  Feel free to edit the repo and uncomment this section
so that an HTML page can be generated for a Web UI"""
# @app.route("/")
# def index():
#     # send http response to html template to display the generated graph 
#     return render_template("index.html", title="Your Generated Graph")


if __name__ == "__main__":
    app.run(debug=True, port=8080)  # change port number if so desired. 