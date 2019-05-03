import sys
from kivy.uix.anchorlayout import AnchorLayout
from kivy.garden.mapview import MapView, MapMarker, MapSource
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp

#Required for the search screen to work
Builder.load_file('layout.kv')

#Search screen, currently no triggers or slots yet
class Search(AnchorLayout):
    pass

#Commented out because maps opens by default not opened when called
"""class Map():
    #https://mapview.readthedocs.io/en/latest/
    #Lat and Lon need to be in the degree decimal format
    latitude = 36.604340
    longitude = -121.854599
    #Min zoom: 0, Max zoom: 20
    magnify = 15
    #Map is provided by default, just needed to pass these values in
    map = MapView(zoom=magnify, lon=longitude, lat=latitude)
    #Open Map
    runTouchApp(map)"""

class Driver(App):
    title = 'Spec Assist'
    def build(self):
        return Search()

#Starts the program
if __name__ == '__main__':
    Driver().run()