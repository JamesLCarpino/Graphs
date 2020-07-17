from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

#going to need a way to travelbackwards when I hit a dead end to a room with an empty space


#need a dictionary for the maze/graph
visited_maze = {}

# def check_dicection(direction)....?????

def walkabout(player,): #what are the paramenters for this?
    #thining depth first traversal

    #what needs to happen.
    # each time you enter a room, add that room to the dictionary if itsn't already there
    # each time you go a direction record the direction you went and what room is associated with that directoin.
        # {
        #   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
        #   5: {'n': 0, 's': '?', 'e': '?'}
        # }  

    #Have I been to this room before??
       # -----YES----
        #If I have been in this room:
            #check for directions untravelled
                #go that direction
                #record the to the room that that direction gives you ->room[][direction]
        #-----NO-----
        #record the room -> now it is in the visited rooms will go through the yes

    #What happens when you hit an end and there are no options
        #if no directions unknown, or no direction to go

            #go back until you hit room with an unexplored option and follow that to the end
                #requires reversing directions



        
    








# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# traversal path holds the appended values of all directions taken


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
