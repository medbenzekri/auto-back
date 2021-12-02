# my_plugin.py
from PIL import Image
import gi
from gi.repository import GObject
import io,os
# from gi.repository import Ide
import requests
import json
class MyAppAddin(GObject.Object):
    def getcatigory():
        query = {'lat':'45', 'lon':'180'}
        response = requests.get("https://wallhaven.cc/api/v1/search?categories=110",params=query)
        dic=response.json()
        print(dic['data'][0]['path'])
        p = requests.get(dic['data'][0]['path'])
        in_memory_file = io.BytesIO(p.content)
        im = Image.open(in_memory_file)
        im.show()
        im.save("im.jpg")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.system("wget -qO - https://github.com/PRATAP-KUMAR/ubuntu-gdm-set-background/archive/main.tar.gz | tar zx --strip-components=1 ubuntu-gdm-set-background-main/ubuntu-gdm-set-background ")
        # os.system("sudo ./ubuntu-gdm-set-background --image "+dir_path+"/im.jpg")
        os.system("echo  | sudo -S ./ubuntu-gdm-set-background --image "+dir_path+"/im.jpg")
    def do_load(self, application):
        pass

    def do_unload(self, application):
        print("goodbye")
MyAppAddin.getcatigory()