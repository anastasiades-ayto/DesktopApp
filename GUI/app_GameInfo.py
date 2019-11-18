#Andrew Anastasiades
#This file sets the basic template for a gui framework

import tkinter as tk
from tkinter import ttk
import widget_styles as widgets


class Game_Input(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        widgets.Configure_Styles()
        self["style"] = "GrayBG.TFrame"
        self.pack(expand=1, fill=tk.BOTH)
        self.create_widgets()

    ##BUTTON FUNCTIONALITY
    def save_input(self):
        self.num_of_players_str = self.enter_number_box.get()
        try:
            self.num_of_players.set(int(self.num_of_players_str))
        except:
            self.num_of_players_str = "<invalid input>"
        self.display_inputs_label.configure(text="Game type: "+ self.game_type.get()+ "\n"+ "Number of Players: "+ self.num_of_players_str)


    ##INSANTIATE WIDGETS
    def create_widgets(self):
        ##VARIABLES
        game_types = ("Heterosexual", "Bisexual")
        self.game_type = tk.StringVar()
        self.num_of_players = tk.IntVar()

        ##OUTER CONTAINER
        self.OUTER = ttk.Frame(self, style='GrayBG.TFrame')
        self.OUTER.pack(padx=10, pady=10, ipadx=25)
        ##CREATE CONTAINERS - LEFT, RIGHT
        self.left_frame = ttk.Frame(self.OUTER, style='GrayBG.TFrame')
        self.right_frame = ttk.Frame(self.OUTER, style='GrayBG.TFrame')
        ##PLACE CONTAINERS
        self.left_frame.pack(side="left", expand=1, fill=tk.BOTH)
        self.right_frame.pack(side="right", expand=1, fill=tk.BOTH)
        
        
        ##LEFT FRAME CREATE ELEMENTS
        self.select_game_label = ttk.Label(self.left_frame, text="Select the game type:", style='GrayBG.TLabel')
        self.select_number_label = ttk.Label(self.left_frame, text="Enter the number of players", style="GrayBG.TLabel")
        self.display_inputs_label = ttk.Label(self.left_frame, style="GrayBG.TLabel")
        ##LEFT FRAME PLACE ELEMENTS
        self.select_game_label.pack()
        self.select_number_label.pack()
        self.display_inputs_label.pack()

        ##RIGHT FRAME CREATE ELEMENTS
        self.game_box = ttk.Combobox(self.right_frame, width=15, textvariable=self.game_type, values=game_types, style="GrayBG.TCombobox")
        self.enter_number_box = ttk.Entry(self.right_frame, width=17, style="GrayBG.TEntry")
        self.save_game_button = ttk.Button(self.right_frame, text="Save", command=self.save_input, style='GrayBG.TButton')
        ##RIGHT FRAME PLACE ELEMENTS
        self.game_box.pack()
        self.enter_number_box.pack()
        self.save_game_button.pack()

