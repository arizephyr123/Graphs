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
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} of {len(room_graph)} rooms visited")



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
###########


# create hash_map with entry for each room
hash_map = {}
for num in range(len(room_graph)):
    hash_map[num] = {'?':'?'}



# puts visited rooms into hashmap
def record_room(room):
    print('**start record room')
    temp = {}
    for ext in room.get_exits():
        print('ext', ext)
        next_room_id = room.get_room_in_direction(ext).id
        print('record_room next id ->', next_room_id)
        temp[ext] = next_room_id
        print('temp', temp)
    hash_map[room.id] = temp
    print('**STOP record room')

# random direction
def rand_direc(valid_exits):
    # print('** rand_direc START **')
    # print('valid_exits', valid_exits)
    num_exits = len(valid_exits)
    # print('num_exits', num_exits)
    rd_int = random.randint(1, num_exits-1)
    # print('rd_int', rd_int)
    # print(f'valid_exits[{rd_int}] -> ', valid_exits[rd_int])
    # print('** rand_direc STOP **')
    return valid_exits[rd_int]

# moves player in dft, then bft while tracking the moves
def move_player():
    print('** move_player START **')
    # print('coords', player.current_room.get_coords())
    room = player.current_room
    exits_all = room.get_exits()
    # print('room', room)

    # get random direction
    rd = rand_direc(exits_all)
    # exit_to_dir = f'{rd}_to'
    print('current', room.id)
    print('exits', exits_all)
    next_in_rd = room.get_room_in_direction(rd).id
    print('in visited? ', next_in_rd in visited_rooms)
    print(f'room in {rd} direction -> {next_in_rd}')
    print('next_in_rd', next_in_rd)


    print(hash_map.keys())
        
    # while the next room in current direction is not in visited rooms
    # while next_in_rd is not None:

    if hash_map[room.id] is '?':
        record_room(room)
    player.travel(rd)
    # update room to new room 
    room = player.current_room
    # add move to traversal path
    traversal_path.append(rd)
    

    print('** move_player STOP **')
    print(traversal_path)



move_player()

for room in hash_map:
    print(f'{room}: {hash_map[room]}')



