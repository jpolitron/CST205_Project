import sys
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.garden.mapview import MapView, MapMarker, MapSource
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty

#Required for the search screen to work
Builder.load_file('layout.kv')

#Used to pass values into MapView
map_info = {
    'latitude' : 0,
    'longitude' : 0,
    'zoom' : 0,
    'route' : []
}

#Changes between the ID entry and Map screens
class Manager(ScreenManager):
    pass

#Map screen
class Map(Screen):
    pass
    """#https://mapview.readthedocs.io/en/latest/
    #Lat and Lon need to be in the degree decimal format
    #Min zoom: 0, Max zoom: 20
    #Map is provided by default, just needed to pass these values in
    map = MapView(zoom=map_info['zoom'], lon=map_info['longitude'], lat=map_info['latitude'])
    #Open Map
    runTouchApp(map)"""

#Search screen, currently no triggers or slots yet
class Search(Screen):
    #Supposed to change the map_info dictionary
    def find_runner(self):
        text = self.ids.runnerID.text
        if text == 'csumb2019':
            map_info['latitude'] = 36.604340
            map_info['longitude'] = -121.854599
            map_info['zoom'] = 15
            map_info['route'].append((36.604340, -121.854599))
            map_info['route'].append((36.602593, -121.848712))
            map_info['route'].append((36.602252, -121.853591))
            map_info['route'].append((36.607573, -121.855879))
        print(map_info)
        #print(self.manager.ids.trackingmap.ids.lat, self.manager.ids.trackingmap.ids.lat)
        self.manager.current = 'map'

class Driver(App):
    title = 'Spec Assist'
    def build(self):
        return Manager()

#Starts the program
if __name__ == '__main__':
    Driver().run()