#Andrew Anastasiades
#Are You The One
#Input/Output Tools
#Object Hierarchy:
#   -Loaders
#       -AppLoader
#       -GameLoader
#   -Savers
#       -GameSaver
#       -AppSaver


import GLOBAL
import pickle

class Saver:

    def __init__(self, namespace='temp'):
        self.namespace = namespace

    def save_obj(self, obj=None, file_identifier='Temp'):
        filename = self.namespace+file_identifier+'.pkl'
        with open(filename, 'wb') as output_file:
            pickle.dump(obj, output_file, pickle.HIGHEST_PROTOCOL)

    
class Loader:
    def __init__(self, namespace='temp'):
        self.namespace = namespace
    
    def load_obj(self, file_identifier='Temp'):
        filename = self.namespace+file_identifier+'.pkl'
        with open(filename, 'rb') as input_file:
            return pickle.load(input_file)
