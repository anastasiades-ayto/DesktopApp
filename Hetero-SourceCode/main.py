#Andrew Anastasiades
#Are You The One
#Final Program Restructuring

import GLOBAL

import structures as struct
import io_tools as io

window_loader = io.Loader(GLOBAL.app_namespace)
window_saver = io.Saver(GLOBAL.app_namespace)

try:
    Window = window_loader.load_obj(GLOBAL.app_file)
    print(GLOBAL.continued_loadup_msg)
except:
    print(GLOBAL.initial_loadup_msg)
    Window = struct.App()


Window.print_games()

window_saver.save_obj(Window, GLOBAL.app_file)




