from keys import *
from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
#import gmplot package
from gmplot import gmplot

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
    #Caasi's Phone Coordinates
    gmap3 = gmplot.GoogleMapPlotter(36.6707, 
                                        -121.6049, 13) #30.3164945 , 78.03219179999999
    latitude_list = [36.6707, 36.6570, 36.65718] #[ 30.3358376, 30.307977, 30.3216419 ] 
    longitude_list = [-121.6049, -121.7952, -121.7927] #[ 77.8701919, 78.048457, 78.0413095 ]
    # scatter method of map object  
    # scatter points on the google map 
    gmap3.scatter( latitude_list, longitude_list, '#FF0000', 
                              size = 40, marker = False ) 
    # Plot method Draw a line in 
    # between given coordinates 
    gmap3.plot(latitude_list, longitude_list,  
               'cornflowerblue', edge_width = 5) 
    
    #Creates a new webpage
    gmap3.draw("templates/map.html")
    sndmap = Map(
        identifier="sndmap",
        lat=36.6707, #37.4419
        lng=-121.6049, #-122.1419
        #MAKE A ROUTE IN CSUMB AND PLOT MY COORDINATES ON THE ROUTE
        #AND OUTPUT "RUNNER ID#CSUMB IS HERE"
        markers=[
          {
              #Caasi's Phone Coordinates
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 36.6707, #37.4419
             'lng': -121.6049, #-122.1419
             'infobox': "<b>Hello World</b>"
          },
          {
            #Runner's Marker
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 36.65718, 
             'lng': -121.7927, 
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('map.html')
    #return render_template('index.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
