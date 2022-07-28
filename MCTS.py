import random
import copy
import math

class Game:
    def __init__(self):
        self.gamestate = []

    def rand_child(self, child):  # this function creates a random child from the given node
        state = child
        indice = [index for (index, item) in enumerate(state[0]) if item == 0]
        random_ind = random.choice(indice)
        if sum(state[0]) > 0:
            state[0][random_ind] = -1
        else:
            state[0][random_ind] = 1
        state[1] = -state[1]
        return state

    def random_simulation(self, child, number_of_simulations):
        # this function randomly simulates ''n = number_of_simulations times'' the entire game from the given node, calculates the value of terminal node and
        # returns the given node with the updated value and number of visits
        depth = child[0].count(0)
        for j in range(number_of_simulations):
            childs = [copy.deepcopy(child)]
            childs[0][2] = 0
            for i in range(depth):
                childs.append(self.rand_child(childs[i]))
            value = self.value_policy(childs[0])[2]
            if value * child[1] > 0:
                child[2] += value
                child[3] += 1
            child[4] += 1
        print(childs[0])
        return child

    def value_policy(self, child):  # raises the value of each side: (2 or -2 for 2 in a row, 3 or -3 for 3 in a row and 4 or -4 for 4 in a row)
        game_length = len(child[0])
        win_minus, win_postive = 0, 0
        for j in range(2, int(game_length / 2) + 1):
             for i in range(len(child[0])):
                if sum(child[0][i:i + j]) == -j:
                    win_minus += -j
                if sum(child[0][i:i + j]) == j:
                    win_postive += j
        child[2] = win_postive + win_minus
        return child


    def expand(self, child):  # expands all the possible childs of a given node
        childs = [copy.deepcopy(child) for i in range(len(child[0]))]
        todelete_indices = []
        for i in range(len(child[0])):
            if childs[i][0][i] == 0:
                childs[i][0][i] = child[1]
            else:
                todelete_indices.append(i)
        return [result for i, result in enumerate(childs) if i not in todelete_indices]

    def UCT_factor(self, child):
        return


    def update(self, state):
        self.gamestate.append(state)

    def __str__(self):
         return "%s" % (self.gamestate)
