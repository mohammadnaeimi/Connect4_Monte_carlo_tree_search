import random
import copy
import math

class Game:
    def __init__(self):
        self.gamestate = []

    def rand_child(self, child):  # this function creates a random child from the given node
        indice = [index for (index, item) in enumerate(child[0]) if item == 0]
        random_ind = random.choice(indice)
        child[0][random_ind] = child[1]
        child[1] = -child[1]
        return child

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
        if child[5] == 0:
            childs = [copy.deepcopy(child) for i in range(len(child[0]))]
            todelete_indices = []
            for i in range(len(child[0])):
                if childs[i][0][i] == 0:
                    childs[i][0][i] = child[1]
                else:
                    todelete_indices.append(i)
            return [result for i, result in enumerate(childs) if i not in todelete_indices]
        else:
            return

    def selection(self, childs):
        list_value = []
        for i in childs:
            list_value.append(i[2])
        return childs[list_value.index(max(list_value))]

    def UCT_factor(self, child):
        child[6] = (child[3] / child[4]) + math.sqrt(2) * math.sqrt(math.log(2 * child[3] / child[3]))
        return child


    def update(self, state):
        self.gamestate.append(state)

    def __str__(self):
         return "%s" % (self.gamestate)
