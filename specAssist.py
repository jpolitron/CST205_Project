import sys
from kivy.uix.anchorlayout import AnchorLayout
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp

#Required for the search screen to work
Builder.load_file('layout.kv')

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

#Search screen, currently no triggers or slots yet
class Search(AnchorLayout):
    pass

class Map():
    #https://mapview.readthedocs.io/en/latest/#mapview.MapSource
    kwargs = {}
    #Supposed to go in the url
    x = 36.654131
    y = -121.798172
    z = 1
    if len(sys.argv) > 1:
        #Open source map, currently defaults to entire earth zoomed out
        kwargs["map_source"] = MapSource(url="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", attribution="")
    #Opens Map, not yet interactive
    runTouchApp(MapView(**kwargs))

class Driver(App):
    title = 'Spec Assist'
    def build(self):
        #Currently set to Map() for debugging
        return Map()

#Starts the program
if __name__ == '__main__':
    Driver().run()