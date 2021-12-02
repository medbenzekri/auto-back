# my_plugin.py

import gi
from gi.repository import GObject
# from gi.repository import Ide
import requests

class MyAppAddin(GObject.Object):
    def getcatigory():
        query = {'lat':'45', 'lon':'180'}
        response = requests.get("https://wallhaven.cc/api/v1/search?categories=111",params=query)
        print(response.json())
        

    def do_load(self, application):
        pass

    def do_unload(self, application):
        print("goodbye")
MyAppAddin.getcatigory()