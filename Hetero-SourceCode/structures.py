#Andrew Anasyasiades
#Are You The One
#Defines Data Structures
#Structure Hierarchy:
#App
#   -Game : Equivalent of a single season
#       -Player
#       -Week
#           -Ceremony
#           -Booth

import GLOBAL

class App:
    def __init__(self):
        self.folder = ""
        self.game_list = list()
        self.active_game = ""
    
    def add_game(self, game_name="Sample"):
        self.game_list.append(game_name)
    
    def del_game(self, game_name):
        try:
            self.game_list.remove(game_name)
            print("'"+game_name+"' was deleted")
        except ValueError:
            print("Game not found")
    
    def print_games(self):
        print("The AYTO Application has the following game files:\n")
        for game_name in self.game_list:
            print(game_name)
        print("\n\n")


class Game:

    def __init__(self, name, game_type="Hetero", index_sex="guy"):
        self.name = name
        self.game_type = game_type
        self.week_list = list() #a list of WeekObj
        self.players = { #values are lists of PlayerObj
            "guy"  : list(), 
            "girl" : list(), 
            "all"   : list() 
        }
        self.stage = ""
        self.num_weeks = 0
        self.sex_index = index_sex

    def add_player(self, player=None):
        try:
            sex = player.sex
            self.players[sex].append(player)
            self.players["all"].append(player)
        except:
            print("Game.add_player", GLOBAL.inv_input)

    def add_week(self, week):
        self.week_list.append(week)
        self.num_weeks += 1

    def print_weeks(self):
        print("There are %d weeks associated with the" % (self.num_weeks), self.name, "Game Obj")
        for week in self.week_list:
            print(week)
        print("")
    
    def print_players(self, sex="all"):
        print("Players associated with '"+self.name+"' with 'sex' set to: "+sex)
        for player in self.players[sex]:
            print(player.name, player.index, sep="\t")
        print("")



class Week:

    def __init__(self, game=None, week_num=0, previous_week=None):
        super().__init__()
        self.game = game #GameObj
        self.week_num = int(week_num)
        self.previous = None #WeekObj
        self.next = None #WeekObj
        self.ceremony = None #CeremonyObj
        self.booth = None #BoothObj
        self.state = "start"
        self.sets = { #a dict of SetObj
            "start" : None,
            "afterbooth" : None,
            "afterceremony": None,
            "end" : None
        }
        self.game.add_week(self)
        self.add_previous(previous_week)

    def add_ceremony(self, ceremony=None):
        self.ceremony = ceremony

    def add_booth(self, booth=None):
        self.booth = booth

    def add_previous(self, previous_week=None):
        try:    
            self.previous = previous_week
            previous_week.add_next(self)
        except:
            print("Week.add_previous", GLOBAL.inv_input)

    def add_next(self, next_week=None):
        try:
            self.next = next_week
            next_week.add_previous(self)
        except:
            print("Week.add_next", GLOBAL.inv_input)



class Ceremony:

    def __init__(self, week=None):
        super().__init__()
        self.week = week
        self.game = week.game
        self.pairings = list() #list of tuples: (PlayerObj, PlayerObj)
        self.matches = int()
        self.int_tuples = {
            "guy"    : tuple(), #Integer Tuple 
            "girl"   : tuple(), #Integer Tuple
            "all" : tuple()  #Tuple of Tuples (#,#) 
        }



class Booth:

    def __init__(self, week=None):
        super().__init__()
        self.week = week
        self.game = week.game
        self.pair = tuple() #(PlayerObj, PlayerObj)
        self.is_match = bool()
        self.int_tuples = {
            "guy"    : tuple(), #Integer Tuple (1xn)
            "girl"   : tuple(), #Integer Tuple (1xn)
            "all" : tuple(), #Integer Tuple (1x2)
        }



class Player:

    def __init__(self, game=None, sex="", name="", index= GLOBAL.invalid_char):
        super().__init__()
        self.game = game
        self.sex = sex
        self.name = name
        self.index = index
        game.add_player(self)


