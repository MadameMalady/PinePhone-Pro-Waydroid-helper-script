#!/usr/bin/env python3

# v 0.1.8
# © 2023 GPL 3.0



# developer note, 'About' function under contruction
import sys
import gi
import os
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib

  # Main Application Window:
        
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        
  # Main Application window size:      
        
        self.set_default_size(360, 720)
        
  # Main Application window Title:        
        
        self.set_title("My Waydroid Manager")
        
  # Main Application window, Box 1:
        
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)
        
  # Button 1 Label= 'First Time Setup':
       
        self.button1 = Gtk.Button(label="First-time Setup")
        self.box1.append(self.button1)
        
  # Button 1, button size:
        
        self.button1.set_margin_top(220)
        self.button1.set_margin_bottom(20)
        self.button1.set_margin_start(10)
        self.button1.set_margin_end(10)
        
  # Button 1, Function, ' First_Time_Setup ':       
        
        self.button1.connect('clicked', self.First_Time_Setup)

        
  # Button 2 Label= 'Manage Install'
        
        self.button2 = Gtk.Button(label="Manage Install")
        self.box1.append(self.button2)
        
  # Button 2, button size:
        
        self.button2.set_margin_top(10)
        self.button2.set_margin_bottom(20)
        self.button2.set_margin_start(10)
        self.button2.set_margin_end(10)
        
  # Button 2, Function, ' First_Time_Setup ':       
        
        self.button2.connect('clicked', self.Manage_Install)
        
  # Button 4 Label= 'Help!'
        
        self.button4 = Gtk.Button(label="Help!")
        self.box1.append(self.button4)
        
  # Button 4, button size:
        
        self.button4.set_margin_top(10)
        self.button4.set_margin_bottom(20)
        self.button4.set_margin_start(10)
        self.button4.set_margin_end(10)
        
  # Button 4, Function, ' Help ':       
        
        self.button4.connect('clicked', self.Help)
        
  # Button 5 Label= 'About'
        
        self.button5 = Gtk.Button(label="About")
        self.box1.append(self.button5)
        
  # Button 5, button size:
        
        self.button5.set_margin_top(10)
        self.button5.set_margin_bottom(20)
        self.button5.set_margin_start(10)
        self.button5.set_margin_end(10)
        
  # Button 5, Function, ' About ':               
        
        self.button5.connect('clicked', self.About)
        
  # Main Application Window's Button's Definitions:
        
  # Button 1, Main Application Window, Function = Open a new window.
        
    def First_Time_Setup(self, button):

    # First Time Setup Window:
    
        class FirstTimeSetupWindow(Gtk.ApplicationWindow):
        
            self.header = Gtk.HeaderBar()
            self.set_titlebar(self.header)
            
            
    # Header Bar, left side, back button
            
            self.Back_Button = Gtk.Button(label="Back")
            self.header.pack_start(self.Back_Button)
            self.Back_Button.set_icon_name("go-previous-symbolic")
            
    # Left side of header bar, 'Back_Button' function:
            
            self.Back_Button.connect('clicked', self.Go_Back)
            
    # First Time Setup window size:      
    
            self.set_default_size(360, 720)
            
    # First Time Setup window Title:
            
            self.set_title("My Waydroid Manager")
            
    # First Time Setup window, Box 2:
        
            self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box2)
            
    # Button 6 Label= 'Install Dependencies':
            
            self.button6 = Gtk.Button(label="Install Dependencies")
            self.box2.append(self.button6)
            
    # Button 6, button size:
            
            self.button6.set_margin_top(300)
            self.button6.set_margin_bottom(20)
            self.button6.set_margin_start(10)
            self.button6.set_margin_end(10)
            
    # Button 6, Function, ' Install_Dependencies ':       
            
            self.button6.connect('clicked', self.Install_Dependencies)
            
  # Install Waydroid Window's Button's Definitions:
        
  # Button 2, Main Application Window, Function = Open a new window.
        
    def Manage_Install(self, button):
        # create a second application window to be called by a button from the primary application window.
 
        class Manage_Install(Gtk.ApplicationWindow):
        
            self.header = Gtk.HeaderBar()
            self.set_titlebar(self.header)
            
            
            # Header Bar, left side, back button
            
            self.Back_Button = Gtk.Button(label="Back")
            self.header.pack_start(self.Back_Button)
            self.Back_Button.set_icon_name("go-previous-symbolic")
            
            
            # Left side of header bar, 'Back_Button' function:
            
            self.Back_Button.connect('clicked', self.Go_Back)            
    
            self.set_default_size(360, 720)
            self.set_title("My Waydroid Manager")
            
            # Third Box, needed to put buttons inside of.
        
            self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box3)
            
            
            
    # Button 7 Label= 'Purge Waydroid Installation':
        
            self.button7 = Gtk.Button(label="Purge Waydroid Installation")
            self.box3.append(self.button7)
            
    # Button 7, button size:
            
            self.button7.set_margin_top(200)
            self.button7.set_margin_bottom(20)
            self.button7.set_margin_start(10)
            self.button7.set_margin_end(10)
            
    # Button 7, Function, ' Purge_Waydroid_Installation ':       
            
            self.button7.connect('clicked', self.Purge_Waydroid_Installation)
            
            
            
    # Button 9 Label= 'Purge Waydroid Images':
    
    
            self.button9 = Gtk.Button(label="Purge Waydroid Images")
            self.box3.append(self.button9)
            
            
    # Button 9, button size:
            
            self.button9.set_margin_top(10)
            self.button9.set_margin_bottom(20)
            self.button9.set_margin_start(10)
            self.button9.set_margin_end(10)
            
    # Button 9, Function, ' Purge_Waydroid_Images ':       
            
            self.button9.connect('clicked', self.Purge_Waydroid_Images)
            
            
            
            # Ninth button, second window, 'Install Waydroid'
            
            self.button9 = Gtk.Button(label="Install Waydroid")
            self.box3.append(self.button9)
            self.button9.set_margin_top(10)
            self.button9.set_margin_bottom(20)
            self.button9.set_margin_start(10)
            self.button9.set_margin_end(10)
            self.button9.connect('clicked', self.Install_Waydroid)
            
            
#-----------------------------------------------------------------------------------------------------
           
    # This is where we will define what each button Does, and connect a function to each of them.
    
        
    #Button 3  
    def Advanced_Options(self, button):
        print("here's some more text, developer.")
      
    #Button 4    
    def Help(self, button):
        print("helpful text!")
    
    #Button 5
    def About(self, button):
        print("Informative texty stuffs")
        
        
        class About_Window(Gtk.ApplicationWindow):
        
            self.header = Gtk.HeaderBar()
            self.set_titlebar(self.header)
            
            
            # Header Bar, left side, back button
            
            self.Back_Button = Gtk.Button(label="Back")
            self.header.pack_start(self.Back_Button)
            self.Back_Button.set_icon_name("go-previous-symbolic")
            
            
            # Left side of header bar, 'Back_Button' function:
            
            self.Back_Button.connect('clicked', self.Go_Back)
    
            self.set_default_size(360, 720)
            self.set_title("My Waydroid Manager")
            
            # Fourth Box, About Window
        
            self.box4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box4)
            
            
            
    # Button 10 Label= 'About':
        
            self.button10 = Gtk.Button(label="My Waydroid Manager GPL 3.0 ©2023" "made with caffine by Kharra Oswin")
            self.box4.append(self.button10)
            
    # Button 10, button size:
            
            self.button10.set_margin_top(300)
            self.button10.set_margin_bottom(20)
            self.button10.set_margin_start(10)
            self.button10.set_margin_end(10)
            
    # Button 10, Function, ' Purge_Waydroid_Installation ':       
            
            self.button10.connect('clicked', self.About)
        
    #Button 6
    def Install_Dependencies(self, button):
        # install dependencies for Waydroid
        print("Installing Dependencies, please wait...")
        os.system("cd scripts && ./dependencies.sh")
            
    #Button 7
    def Purge_Waydroid_Installation(self, button):
        # Purge Waydroid Installation
        print("This will completely remove waydroid")
        os.system("cd scripts && ./purge.sh")  
      
    #Button 9
    def Purge_Waydroid_Images(self, button):
        # Purge Waydroid Images
        print("This will delete all waydroid images and directories")
        os.system("cd scripts && ./purge_images.sh")  
        
    #Button 9
    def Install_Waydroid(self, button):
        # run 'build.sh' to try and build or install waydroid
        print("Installing Waydroid, please wait..")
        os.system("cd scripts && ./build.sh")
        
# This tells the app how to open Various Windows, And close them.
    
# This is where the 'Back' button needs to be defined:
    def on_activate(self, app):
        self.win = FirstTimeSetupWindow(application=app)
        self.win.present()
        FirstTimeSetupWindow = Gtk.ApplicationWindow()
        FirstTimeSetupWindow.connect("destroy", Gtk.ApplicationWindow)
        FirstTimeSetupWindow.show()
        
    def on_activate(self, app):
        self.win = InstallWaydroidWindow(application=app)
        self.win.present()
        InstallWaydroidWindow = Gtk.ApplicationWindow()
        InstallWaydroidWindow.connect("destroy", Gtk.ApplicationWindow)
        InstallWaydroidWindow.show()
        
    def on_destroy(self, widget):
        widget.destroy()
        
            #Button 8
    def Go_Back(self, button):
        # Go back ot the previous Window
        print("going back!")
        self.win = MainWindow(application=app)
        self.win.present()
        
# These lines tell the app what window to open when the app is launched
        
class MyWaydroidManager(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyWaydroidManager(application_id="app.Keo.MyWaydroidManager")
app.run(sys.argv)
