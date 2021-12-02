# my_plugin.py
from PIL import Image
import gi
from gi.repository import GObject
import io
import requests
import json
import os
import subprocess
class MyAppAddin(GObject.Object):
    def getcatigory():
        response = requests.get("https://wallhaven.cc/api/v1/search?categories=110")
        dic=response.json()
        path=dic['data'][0]['path']
        print(path)
        p = requests.get(path)
        in_memory_file = io.BytesIO(p.content)
        im = Image.open(in_memory_file)
        fname="img.png"
        im.save(fname)
        dirpath=f"{os.path.dirname(os.path.realpath(__file__))}/{fname}"
        subprocess.call(f" ./script --image '{dirpath}'",shell=True)


    def do_load(self, application):
        pass

    def do_unload(self, application):
        print("goodbye")
MyAppAddin.getcatigory()