#Andrew Anastasiades
#Main Menu for GUI

##IMPORT 3RD PARTY PACKAGES
import tkinter as tk
from tkinter import ttk

##IMPORT LOCAL GUI DEPENDENCIES
from app_GameInfo import Game_Input
from app_NamePlayers import Name_Players
import widget_styles as widgets

##VARIABLES
#   -none for now


##INITIALIZE WINDOW
window = tk.Tk()
window.geometry("500x500+750+0")
window.title("Are You The One?")


##LOAD WIDGET STYLES
widgets.Configure_Styles()


##INITIALIZE MAINFRAME
mainframe = ttk.Notebook(window, style='TNotebook')
mainframe.pack(expand=1, fill=tk.BOTH)


##ADD TABS TO MAINFRAME
#Game Inputs
tab1 = Game_Input(mainframe)
mainframe.add(tab1, text="Game Inputs")
#Misc
tab2 = Name_Players(mainframe)
mainframe.add(tab2, text="Player Names")

##DEBUG


##EXECUTE APPLICATION
print("Application Beginning......")
window.mainloop()
print(".....Application Terminated")
