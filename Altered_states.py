#Altered states

#Make the 5x5 grid by getting the input
import numpy as np
from collections import Counter
import time
#list of states
state_populations = {
    "california": 39538223,
    "texas": 29145505,
    "florida": 21538187,
    "newyork": 20201249,
    "pennsylvania": 13002700,
    "illinois": 12812508,
    "ohio": 11799448,
    "georgia": 10711908,
    "northcarolina": 10439388,
    "michigan": 10077331,
    "newjersey": 9288994,
    "virginia": 8631393,
    "washington": 7693612,
    "arizona": 7151502,
    "massachusetts": 7029917,
    "tennessee": 6910840,
    "indiana": 6785528,
    "missouri": 6154913,
    "maryland": 6177224,
    "wisconsin": 5893718,
    "colorado": 5773714,
    "minnesota": 5706494,
    "southcarolina": 5118425,
    "alabama": 5024279,
    "louisiana": 4657757,
    "kentucky": 4505836,
    "oregon": 4237256,
    "oklahoma": 3959353,
    "connecticut": 3605944,
    "utah": 3271616,
    "iowa": 3190369,
    "nevada": 3104614,
    "arkansas": 3011524,
    "mississippi": 2961279,
    "kansas": 2937880,
    "newmexico": 2117522,
    "nebraska": 1961504,
    "westvirginia": 1793716,
    "idaho": 1839106,
    "hawaii": 1455271,
    "maine": 1362359,
    "newhampshire": 1377529,
    "montana": 1084225,
    "rhodeisland": 1097379,
    "delaware": 989948,
    "southdakota": 886667,
    "northdakota": 779094,
    "alaska": 733391,
    "vermont": 643077,
    "wyoming": 576851
}


def string_to_2d_array(s):
    if len(s) != 25:
        raise ValueError("The string must be exactly 25 characters long.")
    
    # Create the 2D array
    array_2d = []
    for i in range(0, 25, 5):
        row = list(s[i:i+5])
        array_2d.append(row)
    
    return array_2d


def all_or_all_but_one_letters_in_string(short_string, long_string):
    short_counter = Counter(short_string)
    long_counter = Counter(long_string)
    
    missing_count = 0
    
    for char, count in short_counter.items():
        if long_counter[char] < 1: #if not in long string add one to count
            missing_count += 1
        if missing_count > 1:
            return False
    
    return True


#checks the 
def possible_states_in_grid(grid):
    states = []
    for state in state_populations.keys():
        if(all_or_all_but_one_letters_in_string(state, grid)):
            states.append(state)
    return states


def get_total_population(states):
    sum = 0
    for state in states:
        sum += state_populations.get(state)

    return sum


def states_in_grid(grid):
    grid_matrix = string_to_2d_array(grid)
    for state in possible_states_in_grid(grid):
        return

def get_start_position(grid, target):
    start_pos = []
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == target:
                start_pos.append([x,y])
    
    return start_pos

def king_move(grid, x, y, target):
    moves = []
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i>= 0 and i<len(grid) and j>=0 and j<len(grid) and (not (i==x and j ==y)):
                if grid[i][j] == target or target == '5':
                    moves.append([i,j])
    
    return moves                

def cords_not_visited(counter, grid_size):
    list = []
    for x in range(grid_size):
        for y in range(grid_size):
            if tuple([x,y]) not in counter:
                list.append(tuple[x,y])
    return list

def recursiontest(grid, state, start_coordinate, i, start_string, joker):
    if start_string == state:
        cords_seen.append(tuple(start_coordinate))
        return True
    else:  
        if (not king_move(grid, start_coordinate[0], start_coordinate[1], state[i])) == False:
            start_string = start_string + state[i]
            for cord in king_move(grid, start_coordinate[0], start_coordinate[1], state[i]):
                if recursiontest(grid,state,cord,i+1, start_string, joker):
                    cords_seen.append(tuple(cord))
                    return True
        else:
            if joker: 
                start_string = start_string + state[i]
                for cord in king_move(grid, start_coordinate[0], start_coordinate[1], '5'):
                    if recursiontest(grid,state,cord,i+1, start_string, False):
                        cords_seen.append(tuple(cord))
                        return True 
        if joker:
            for cord in king_move(grid, start_coordinate[0], start_coordinate[1], '5'):
                 
                    
                    if recursiontest(grid,state,cord,i+1, start_string, False):
                        cords_seen.append(tuple(cord))
                        return True
                        
def missing_states(list_states):
    missing_states = {}
    for state, population in state_populations.items():
        if state not in list_states:
            missing_states.update({state: population})
    return sorted(missing_states.items(), key=lambda item: item[1], reverse=True)

def find_all_states(grid):
    possible_states = possible_states_in_grid(grid)
    grid = string_to_2d_array(grid)
    all_states = []
    for state in possible_states:
        if not get_start_position(grid, state[0]):
            state_alt = state[1:]
            for coords in get_start_position(grid, state_alt[0]):
                if recursiontest(grid, state_alt, coords,1, state_alt[0], False):
                    cords_seen.append(tuple(coords))
                    all_states.append(state)
                    break
        for coords in get_start_position(grid, state[0]):
            if recursiontest(grid, state, coords,1, state[0], True):
                all_states.append(state)
                cords_seen.append(tuple(coords))
                break
        state_alt = state[1:]
        if state not in all_states:
            for coords in get_start_position(grid, state_alt[0]):
                if recursiontest(grid, state_alt, coords,1, state_alt[0], False):
                    cords_seen.append(tuple(coords))
                    all_states.append(state)
                    break
    return all_states
    
def print_output(grid):
    print("--------------")
    print("score", get_total_population(find_all_states(grid)), find_all_states(grid))
    print("-------------")
    print("largest missing states:", missing_states(find_all_states(grid)))
def joker(grid, state):
    altered_state = []
    for c in list(state):
        return
    
def replace_chars_with_x(s):
    result = []
    for i in range(len(s)):
        # Replace the i-th character with 'x'
        new_string = s[:i] + 'x' + s[i+1:]
        result.append(new_string)
    return result
           
st = 'aaska'
start_time = time.time()
cords_seen = []

# print("--- %s seconds ---" % (time.time() - start_time))
# print("score", get_total_population(find_all_states('akweolyhmnaiodaxefritlogn')), find_all_states('akweolyhmnaiodaxefritlogn'))
# counter = {}

# print("largest missing states:", missing_states(find_all_states('akweolyhmnaiodaxefritlogn')))
#print("test the recursion:", recursiontest(string_to_2d_array(), 'alaska',[0,0],1, 'a'))




print_output("marogntseiasewalinyhforku")
counter = {}
list_cords = []
for x in range(5):
        for y in range(5):
            list_cords.append(tuple([x,y]))
for cord in cords_seen: 
    if cord not in counter:
        counter[cord] = 0
    counter[cord] += 1
print(counter)
for x in range(5):
        for y in range(5):
            if tuple([x,y]) in cords_seen:
                if counter[tuple([x,y])] == 3:
                    print([x,y])
# tested: marogntseiasejalinwdforka, clfrgaionikrsnadweaeayetx
