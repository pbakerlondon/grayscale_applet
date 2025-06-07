#!/usr/bin/env python

# Name: grayscale_applet.py
# Description: The script starts a system tray applet that uses an application "vibrant-cli" (https://github.com/libvibrant/libvibrant) to change all displays to grayscale mode and back.
# Author: Thomas L.C. van Houten
# Date Created: 2023-05-07
# Last Modified: 2023-06-13
# Version: 0.0.6
# Tested on: Linux Mint 21.1 Vera, Kernel 5.15.0-73-generic x86_64, Desktop: Xfce 4.16.0, CPU: Intel Core i5-9400F, GPU: AMD Radeon RX 6600 XT, Driver: amdgpu, OpenGL: 4.6 Mesa 22.2.5, RAM: 31.29 GiB

# Additional Notes:
# "gir1.2-appindicator3-0.1" and xrandr are needed. Also, the vibrant-cli needs to be built and located at $HOME/Applications/libvibrant/build/vibrant-cli/vibrant-cli

import gi
gi.require_version('Gtk', '3.0') # Require version of GTK library
gi.require_version('AppIndicator3', '0.1') # Require version of AppIndicator3 library
from gi.repository import Gtk # Import GTK module
from gi.repository import AppIndicator3 as appindicator # Import AppIndicator3 module
import subprocess # Import subprocess module
import os # Import os module

class GrayscaleApplet:
    def __init__(self):
        self.indicator = appindicator.Indicator.new(
            "grayscale-applet",
            "display",
            appindicator.IndicatorCategory.APPLICATION_STATUS) # Create an indicator object
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE) # Set the indicator status
        self.indicator.set_menu(self.create_menu()) # Set the menu for the indicator

    def create_menu(self):
        menu = Gtk.Menu() # Create a menu object

        item_grayscale = Gtk.MenuItem('Grayscale mode') # Create a menu item for grayscale mode
        item_grayscale.connect('activate', self.set_grayscale) # Connect the grayscale mode menu item to set_grayscale method
        menu.append(item_grayscale) # Add grayscale mode menu item to the menu

        item_normal = Gtk.MenuItem('Normal mode') # Create a menu item for normal mode
        item_normal.connect('activate', self.set_normal) # Connect the normal mode menu item to set_normal method
        menu.append(item_normal) # Add normal mode menu item to the menu

        item_sep = Gtk.SeparatorMenuItem() # Create a separator between menu items
        menu.append(item_sep) # Add the separator to the menu

        item_about = Gtk.MenuItem('About') # Create a menu item for the about page
        item_about.connect('activate', self.about) # Connect the about menu item to about method
        menu.append(item_about) # Add about menu item to the menu

        item_quit = Gtk.MenuItem('Quit') # Create a menu item for quitting the applet
        item_quit.connect('activate', self.quit) # Connect the quit menu item to quit method
        menu.append(item_quit) # Add quit menu item to the menu

        menu.show_all() # Show all menu items
        return menu

    def set_grayscale(self, widget):
        self.run_vibrant_cli("0") # Run vibrant-cli with the argument for grayscale mode

    def set_normal(self, widget):
        self.run_vibrant_cli("1") # Run vibrant-cli with the argument for normal mode

    def about(self, widget):
        about_dialog = Gtk.AboutDialog()
        about_dialog.set_program_name("Grayscale Applet")
        about_dialog.set_version("0.0.7")
        about_dialog.set_authors(["Thomas L.C. van Houten"])
        about_dialog.set_comments("This applet uses vibrant-cli to switch between grayscale and normal display modes.")
        about_dialog.set_website("https://github.com/libvibrant/libvibrant")
        about_dialog.run()
        about_dialog.destroy()

    def run_vibrant_cli(self, value):
        vibrant_cli = os.path.expanduser("~/Applications/libvibrant/build/vibrant-cli/vibrant-cli")
        # Loop through all connected displays and set the grayscale value
        monitors = subprocess.check_output(['xrandr', '--listmonitors']).decode('utf-8').splitlines()[1:]
        for monitor in monitors:
            display = monitor.split()[-1]
            command = [vibrant_cli, display, value]
            subprocess.Popen(command) # Run the command

    def quit(self, widget):
        Gtk.main_quit() # Quit the GTK main loop

def main():
    Gtk.init() # Initialize GTK
    applet = GrayscaleApplet() # Create an instance of GrayscaleApplet
    Gtk.main() # Start the GTK main loop

if __name__ == "__main__":
    main() # Call the main function if the script is run directly

