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


# holds the {n:?, s:?...}
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# traversal path holds the appended values of all directions taken
# going to need a way to travelbackwards when I hit a dead end to a room with an empty space
reverse = {"n": "s", "s": "n", "e": "w", "w": "e"}
# should be able to call the above for the reversing the direction

#   what needs to happen.
# each time you enter a room, add that room to the dictionary if itsn't already there
# each time you go a direction record the direction you went and what room is associated with that directoin.
# {
#   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#   5: {'n': 0, 's': '?', 'e': '?'}
# }

# beign the depth first traversal


def find_the_way(visited_rooms=None):

    direction_store = []

    if visited_rooms is None:
        visited_rooms = []
    visited_rooms.append(player.current_room.id)

    # get the possible direction out of the currentroom
    for ways_out in player.current_room.get_exits():
        # now move in a direction
        player.travel(ways_out)
        # has this room been visisted? YES
        if player.current_room.id not in visited_rooms:
            # record the room -> now it is in the visited rooms
            visited_rooms.append(player.current_room.id)
            # record the direction to the direction store
            direction_store.append(ways_out)
            # recurse through using the same rules since its now in the visited room
            # do not try to set a new variable and loop through causes a wild and crazy infinite loop. yeesh.
            direction_store += find_the_way(visited_rooms)
            print(direction_store)

            player.travel(reverse[ways_out])
            direction_store.append(reverse[ways_out])
        # if the room has not been visisted
        else:
            # check untravelled ways
            player.travel(reverse[ways_out])
    return direction_store

    # Have I been to this room before??
    # -----YES----
    # If I have been in this room:
    # check for directions untravelled
    # go that direction
    # record the to the room that that direction gives you ->room[][direction]
    # -----NO-----

    # What happens when you hit an end and there are no options
    # if no directions unknown, or no direction to go

    # go back until you hit room with an unexplored option and follow that to the end
    # requires reversing directions


# set the path to the function to walk the path of resistance, and knowledge
traversal_path = find_the_way()
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
