
NORTH = 1
SOUTH = -1
EAST = 1
WEST = -1

def main():
    movements = input()
    pokemon_caught = readMovements(movements)
    print(pokemon_caught)

# reads each char in movements and changes x and y position accordingly 
# keeps track of a list of tuples containing the positions where we have visited
# adds a pokemon at each bi-dimensional position not visited
def readMovements(movements):
    position_x = 0
    position_y = 0
    pokemons = 1
    pokemon_map = [(0,0)]
    for mov in movements:
        match mov:
            case "N":
                position_y += NORTH
            case "S":
                position_y += SOUTH
            case "E":
                position_x += EAST
            case "O":
                position_x += WEST
            case _:
                raise RuntimeError('Input syntax unknown.')
        if((position_x, position_y) not in pokemon_map):
            pokemons += 1
            pokemon_map.append((position_x, position_y))       
    return pokemons

# comment the next line before running the tests script
main()