import sys
import copy

curr_min = sys.maxsize
q = []
visited = []

def compare(s,g):
    if s==g:
        return(1)
    else:
        return(0)

def find_pos(s):

    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return [i, j]

def up(s,pos):

    i = pos[0]
    j = pos[1]

    if i > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i-1][j]
        temp[i-1][j] = 0
        return temp
    else:
        return s

def down(s,pos):

    i = pos[0]
    j = pos[1]

    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0
        return temp
    else:
        return s

def right(s,pos):

    i = pos[0]
    j = pos[1]

    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0
        return temp
    else:
        return s

def left(s,pos):

    i = pos[0]
    j = pos[1]

    if j > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0
        return temp
    else:
        return s

def enqueue(s):
    global q
    q = q + [s]

def heuristic(s,g):
    d = 0
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j]:
                d += 1
    return d

def steepest_ascent(s, g):
    global curr_min
    curr_state = copy.deepcopy(s)
    if s == g:
        return

    global visited
    while True:
        pos = find_pos(curr_state)
        possible_states = [up(curr_state, pos), down(curr_state, pos), right(curr_state, pos), left(curr_state, pos)]
        best_state = None
        min_h = sys.maxsize

        for state in possible_states:
            h = heuristic(state, g)
            if h < min_h:
                min_h = h
                best_state = state

        if best_state == curr_state:
            print("Steepest ascent hill-climbing stopped at local maximum.")
            return

        if best_state == g:
            print("Goal State found !! The intermediate States are :")
            print(visited + [g])
            return

        if best_state not in visited:
            visited.append(best_state)
            curr_state = best_state
        else:
            print("Steepest ascent hill-climbing stopped at a plateau.")
            return

def main():
    s = [[2, 8, 3], [1, 5, 4], [7, 6, 0]]
    g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    global q
    global visited
    q = q + [s]
    visited = visited + [s]
    steepest_ascent(s, g)

if __name__ == "__main__":
    main()