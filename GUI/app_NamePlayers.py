#Andrew Anastasiades
#APPLICATION - Enter Player Names

import tkinter as tk
from tkinter import ttk
import widget_styles as widgets


class Name_Players(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        widgets.Configure_Styles()
        self["style"]= "GrayBG.TFrame"
        self.pack(expand=1, fill=tk.BOTH)
        self.num_players = 20
        self.game_type = "Hetero"
        ##OUTER CONTAINER
        self.OUTER = ttk.Frame(self, style='GrayBG.TFrame')
        self.OUTER.pack(padx=10, pady=10, ipadx=25)
        ##FILL OUTER CONTAINER
        self.create_widgets()


    ##BUTTON FUNCTIONS
    def update_names(self):
        for i in range(self.num_players):
            self.PLAYER_NAMES[i] = self.entry_boxes[i].get()
        print(self.PLAYER_NAMES.values())

    def update_num_players(self, num_players=18):
        self.num_players = num_players
        for child in self.OUTER.winfo_children():
            child.destroy()
        self.create_widgets()
        

    def create_widgets(self):
        ##VARIABLES
        self.PLAYER_NAMES = dict()
        self.entry_boxes = dict()
        
        ##INNER CONTAINERS - NAME, BUTTONS
        self.name_frame = ttk.Frame(self.OUTER, style='GrayBG.TFrame')
        self.button_frame = ttk.Frame(self.OUTER, style='GrayBG.TFrame')
        ##PLACE INNER CONTAINERS
        self.name_frame.pack(side="top", expand=1, fill=tk.BOTH)
        self.button_frame.pack(side="bottom", expand=1, fill=tk.X)
        
        ##NAME CONTAINERS - LEFT, RIGHT
        self.left_frame = ttk.Frame(self.name_frame, style='GrayBG.TFrame')
        self.right_frame = ttk.Frame(self.name_frame, style='GrayBG.TFrame')
        ##PLACE NAME CONTAINERS
        self.left_frame.pack(side="left", expand=1, fill=tk.BOTH)
        self.right_frame.pack(side="right", expand=1, fill=tk.BOTH)

        ##ITERATIVELY CREATE ENTRIES FOR NAMES
        for i in range(self.num_players):
            if i < (self.num_players/2):
                parent = self.left_frame
            else:
                parent = self.right_frame
            container = ttk.Frame(parent, style="GrayBG.TFrame")
            container.pack()
            label = ttk.Label(container, text=str(i), style="GrayBG.TLabel")
            entry = ttk.Entry(container, width=15, style="TEntry")
            self.entry_boxes[i] = entry
            label.grid(row=0, column=0)
            entry.grid(row=0, column=1)

        ##UPDATE NAMES BUTTON
        self.update_names_button = ttk.Button(self.button_frame, text="Update Names", style='GrayBG.TButton', command=self.update_names)
        self.update_names_button.pack()
        ##UPDATE NUM_PLAYERS BUTTON
        self.update_number_button = ttk.Button(self.button_frame, text="Update Number", style='GrayBG.TButton', command=self.update_num_players)
        self.update_number_button.pack()
