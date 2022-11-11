from PIL import Image
from gi.repository import GObject
import io
import requests
import time
import os
import subprocess as sp
from simple_term_menu import TerminalMenu
def main():
    global fname,dirpath,cmd
    fname="img.png"
    dirpath=f"{os.path.dirname(os.path.realpath(__file__))}/{fname}"
    Screen_choice=Menu(["Lock Screen","Desktop"],"")
    Time_choice=Menu(["hours","minutes","seconds"],"")
    Time=ConvertTime(Time_choice,int(input(f"How many {Time_choice} do you want to: ")))
    if Screen_choice=="Lock Screen":
        cmd=f"sudo ./script --image '{dirpath}'"
    else:
        gset=sp.getoutput("which gsettings")
        cmd=f"{gset} set org.gnome.desktop.background picture-uri {dirpath}"
    dic=getcategory()
    SetWallpaper(dic,Time)

def Menu(options,title):
    terminal_menu = TerminalMenu(options,title=f"{title}")
    index = terminal_menu.show()
    return options[index]

def ConvertTime(Unite,Time):
    if Unite == "minutes":
        Time = int(Time) * 60
    elif Unite == "hours":
        Time = Time * 3600
    return Time

def getcategory():
    response = requests.get(f"https://wallhaven.cc/api/v1/search?q=hill")
    dic=response.json()
    return dic
    
def SetWallpaper(dic,Time):
    print("Script is running...\n")
    for i in range(0,len(dic['data'])):
        path=dic['data'][i]['path']
        p = requests.get(path)
        in_memory_file = io.BytesIO(p.content)
        im = Image.open(in_memory_file)
        im.save(fname)
        os.system(cmd)
        time.sleep(int(Time))

## Main
main()
