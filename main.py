import random
import copy
from MCTS import Game

#input value of all the functions: [[the game state], the play turn(1 or -1), the value of the state, number of times the state is visited

children = []

def rand_child(child): # this function creates a random child from the given node
    state = child
    indice = [index for (index, item) in enumerate(state[0]) if item == 0]
    random_ind = random.choice(indice)
    if sum(state[0]) > 0:
        state[0][random_ind] = -1
    else:
        state[0][random_ind] = 1
    state[1] = -state[1]
    return state

def random_simulation(child, number_of_simulations):
    # this function randomly simulates ''n = number_of_simulations times'' the entire game from the given node, calculates the value of terminal node and
    # returns the given node with the updated value and number of visits
    depth = child[0].count(0)
    for j in range(number_of_simulations):
        childs = [copy.deepcopy(child)]
        childs[0][2] = 0
        for i in range(depth):
            childs.append(rand_child(childs[i]))
        child[2] += value_policy(childs[0])[2]
        child[3] += 1
    return child

def value_policy(child): # raises the value of each side: (2 or -2 for 2 in a row, 3 or -3 for 3 in a row and 4 or -4 for 4 in a row)
    game_length = len(child[0])
    for j in range(2, int(game_length / 2) + 1):
        for i in range(len(child[0])):
            if sum(child[0][i:i+j]) == -j:
                child[2] += -j / 10
            if sum(child[0][i:i+j]) == j:
                child[2] += j / 10
    return child

def expand(child): # expands all the possible childs of a given node
    childs = [copy.deepcopy(child) for i in range(len(child[0]))]
    todelete_indices = []
    for i in range(len(child[0])):
        if childs[i][0][i] == 0:
            childs[i][0][i] = child[1]
        else:
            todelete_indices.append(i)
    return [result for i, result in enumerate(childs) if i not in todelete_indices]

def update(state):
    children.append(state)
    return children[0]


if __name__ == '__main__':
    g = Game()
    simulazion_1 = g.random_simulation([[0, 1, 0, 0], -1, 0, 0], 2)
    simulazion_2 = g.random_simulation([[1, 0, 0, 0], -1, 0, 0], 2)
    g.update(simulazion_1)
    g.update(simulazion_2)
    print(g)