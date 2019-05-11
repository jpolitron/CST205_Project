from keys import *
from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = my_key
GoogleMaps(app, key = my_key)

#For ID input
@app.route("/")
def idEntry():
    return render_template("input.html")

#https://github.com/rochacbruno/Flask-GoogleMaps
@app.route("/", methods=['POST'])
def mapview():
    #Pulls the ID from the previous page
    text = request.form['text']
    #Test error catch system
    if text != 'csumb':
        return render_template("errorpage.html")
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('index.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
