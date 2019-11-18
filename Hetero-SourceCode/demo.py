#Andrew Anastasiades
#Are You The One
#struct of applications

import structures as struct
import io_tools as io

print("\nDemo Beginning...\n")

l = io.Loader("DEMO")
s = io.Saver("DEMO")

temp = l.load_obj("ExampleSeason")
temp.print_players()
temp.print_weeks()

temp.print_players("guy")
temp.print_players("girl")
temp.print_players()
temp.print_weeks()


#s.save_obj(temp, temp.name)

print("\n...Demo Ended\n")

""" Data Demo
temp = struct.Game(name="ExampleSeason", game_type="Hetero", index_sex="guy")
w1 = struct.Week(game=temp)
w2 = struct.Week(temp, 1, w1)
w3 = struct.Week(temp, 2, w2)
w4 = struct.Week(temp, 3, w3)
guy_names = [
    "Andrew",
    "Steve",
    "Michael",
    "John",
    "Chris",
    "Bartholemew"
]
guy_names.sort()
for i in range(len(guy_names)):
    struct.Player(game=temp, sex="guy", name=guy_names[i], index=i)
girl_names = [
    "Tricia",
    "Alicia",
    "Bria",
    "Alexis",
    "Alexis",
    "Belle"
]
girl_names.sort()
for i in range(len(girl_names)):
    struct.Player(game=temp, sex="girl", name=girl_names[i], index=i)
"""
