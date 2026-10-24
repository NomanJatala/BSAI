import numpy as np
state = np.array([
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
])

def travel(new_state,direction):
    moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
    blank_position = np.argwhere(new_state == 0)[0]
    br = blank_position[0]
    bc = blank_position[1]

    # Neighbering point
    dr, dc = moves[direction]

    nr,nc = br+dr , dc+bc
    if not (0 <= nr < new_state.shape[0] and
        0 <= nc < new_state.shape[1]):
        return print("This move is illgel")

    new_state[br,bc], new_state[nr,nc] = new_state[nr,nc], new_state[br,bc]
    return new_state
print(state)
while dir != "exit":
    dir =str(input("Enter direction: "))     
    if dir == "exit":
        print("Good bye")
        break
    print(travel(state,dir))
    print()
