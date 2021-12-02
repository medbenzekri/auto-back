# my_plugin.py

import gi

from gi.repository import GObject
from gi.repository import Ide

class MyAppAddin(GObject.Object, Ide.ApplicationAddin):

    def getcatigory():
        pass

    def do_load(self, application):
        

    def do_unload(self, application):
        print("goodbye")