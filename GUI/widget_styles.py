#Andrew Anastasiades
#Widget Styles

import tkinter as tk
from tkinter import ttk

BASE_STYLES = [ "TButton", "TCheckbutton", "TFrame",
                "TLabel", "TCombobox", "TNotebook",
                "TEntry"]

STYLE_PREFIXES = ["GrayBG."]


def Configure_Default_Style():
    #Define 'Style' object and set theme
    s = ttk.Style()
    s.theme_use('classic')
    #Configure Styles
    s.configure("TButton")
    s.configure("TCheckbutton")
    s.configure("TFrame")
    s.configure("TLabel")
    s.configure("TCombobox")
    s.configure("TNotebook")
    s.configure("TEntry", padx=5, pady=5,)

def Configure_BG_Style(prefix, s_bg):
    #Define 'Style' object and set theme
    s = ttk.Style()
    s.theme_use('classic')
    #Configure Styles
    for each in BASE_STYLES:
        s.configure(prefix+each, background=s_bg)

def Configure_Styles():
    Configure_Default_Style()
    Configure_BG_Style("GrayBG.", "GRAY")
