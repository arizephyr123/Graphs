from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Queue

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
    hash_map[num] = {0: 0}




# get random direction
def rand_direc(valid_exits):
    print('\n** rand_direc START **')
    
    num_exits = len(valid_exits)
    if num_exits == 1:
        print('rd->', valid_exits[0])
        return valid_exits[0]
    else:
        rd_int = random.randint(1, num_exits-1)
    print(f'rd -> {valid_exits[rd_int]}\n**')
    return valid_exits[rd_int]

# get opposite direction
def rev_direc(curr_direct):
    if curr_direct == 'n':
        return 's'
    if curr_direct == 's':
        return 'n'
    if curr_direct == 'e':
        return 'w'
    if curr_direct == 'w':
        return 'e'


# puts room moves into hash_map
def record_room(curr_room, direc, prev_room):
    print(f'\n**start record room\nfrom {prev_room.id} moved {direc} to {curr_room.id}(CURRENT)')
    print(f'curr room exits-> {curr_room.get_exits()}')

    # record next in direction from previous room exit
    hash_map[prev_room.id][direc] = curr_room.id

    temp = {}
    print('temp BEFORE', temp)
    for (k, v) in hash_map[curr_room.id].items():
        if k in curr_room.get_exits():
            if temp[k]:
                pass
            else:
                temp[k] = '?'
    print('temp After', temp)
        
    # record current room exits with curr_room in direction came from
    opposite_direc = rev_direc(direc)
    for ext in curr_room.get_exits():
        if ext == opposite_direc:
                temp[ext] = prev_room.id
        else:
            temp[ext] = '?'
    hash_map[curr_room.id] = temp
    print(f'hash_map[{prev_room.id}][{direc}] = {hash_map[prev_room.id][direc]}\nhash_map[{curr_room.id}][{opposite_direc}] = {hash_map[curr_room.id][opposite_direc]}\n**\n')


# moves player in dft, then bft while tracking the moves
def move_player():
    print('\n** move_player START **')
    room = player.current_room
    exits = room.get_exits()

    # get random direction
    rd = rand_direc(exits)

    print('current room ', room.id)
    print('exits', exits)
    next_in_rd = room.get_room_in_direction(rd).id if room.get_room_in_direction(rd) else None

    # print(f'{next_in_rd} in visited? ', next_in_rd in visited_rooms)
    print(f'room in {rd} direction -> {next_in_rd}')
    # print(f'room in {rd} direction -> {next_in_rd}')
    print('next_in_rd', next_in_rd)
        
    while player.travel(rd) is not None:
        # add move to traversal path
        traversal_path.append(rd)
        # save previous room
        prev_room = room
        # update room to new room, record and update exits
        room = player.current_room
        record_room(room, rd, prev_room)
        exits = room.get_exits()
    
    avail_exits = []
    for ext in avail_exits:
        if hash_map[curr_room][ext] is not '?':
            avail_exits.append(ext)
    print('avail_exits', avail_exits)
    if len(avail_exits) == 0:
        bfs(room)
    else:
        return move_player()
    
    print('** move_player STOP **')
    


#******
def bfs(start_room):
        """
        1.  Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it in your BFS queue like normal.

        2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.
        """
        # queue holds path from start_room to unexplored
        rm_queue = Queue()
        rm_queue.enqueue([start_room])

        checked = set()

        while rm_queue.size() > 0:
            room_path = rm_queue.dequeue()
            # grab last room in room_path
            curr_room = room_path[-1]
            # any unexplored directions?
            if curr_room not in checked:
                print(f'{curr_room.id} not in checked')
                




            # if curr_room == destination_vertex:
            #     return room_path
            # # checked.add(curr_room)
            
            # for neighbor in get_neighbors(curr_room):
            #     # copy room_path and add neighbor
            #     new_path = list(room_path)
            #     new_path.append(neighbor)
            #     rm_queue.enqueue(new_path)


#******
move_player()
print('\n')

for room in hash_map:
    print(f'{room}: {hash_map[room]}')

print(traversal_path)


