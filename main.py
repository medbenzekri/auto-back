# my_plugin.py
from PIL import Image
import gi
from gi.repository import GObject
import io
# from gi.repository import Ide
import requests
import json
class MyAppAddin(GObject.Object):
    def getcatigory():
        query = {'lat':'45', 'lon':'180'}
        response = requests.get("https://wallhaven.cc/api/v1/search?categories=111",params=query)
        dic=response.json()
        print(dic['data'][0]['path'])
        p = requests.get(dic['data'][0]['path'])
        in_memory_file = io.BytesIO(p.content)
        im = Image.open(in_memory_file)
        im.show()

    def do_load(self, application):
        pass

    def do_unload(self, application):
        print("goodbye")
MyAppAddin.getcatigory()