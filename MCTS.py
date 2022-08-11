import random
import copy
import math
from itertools import cycle

class Game:

    def __init__(self, initiate, towin): # input value is a list containing >> 0:State - 1:To_play - 2:Number_of_wins - 3:Number_of_visits - 4:UCT_factor
        self.toplay = towin # the players who's win is simulated
        self.gamestate = [initiate] # the states of the game which have been visited
        self.number_of_total_simulations = 0
        self.selected = [initiate] # the nodes
        self.expanded = []
        self.selection_indice = [0]
        self.current_child = initiate

    def rand_child(self, child):  # this function creates a random child from the given node
        indice = [index for (index, item) in enumerate(child[0]) if item == 0]
        random_ind = random.choice(indice)
        child[0][random_ind] = child[1]
        child[1] = -child[1]
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
        result = win_postive + win_minus
        child[2] = result
        return child

    def UCB_factor(self, i):
        if i[3] == 0:
            i[4] = 100
        else:
            i[4] = round((i[2] / i[3]) + math.sqrt(2) * math.sqrt(math.log(self.number_of_total_simulations) / i[3]), 2)
        return i[4]

    def rollout(self, number_of_simulations):
        child = self.current_child
        depth = child[0].count(0)
        for j in range(number_of_simulations):
            childs = [copy.deepcopy(child)]
            for i in range(depth):
                childs.append(self.rand_child(childs[i]))
            value = self.value_policy(childs[0])[2]
            if value * self.toplay > 0:
                child[2] += 1
            child[3] += 1
            self.number_of_total_simulations += 1
        #self.number_of_total_simulations += 1

    def backpropogation(self): # backpropogates the updated values after rollout (simulation)
        for i in range(len(self.selection_indice) - 1):
            self.gamestate[self.selection_indice[i]][2] += self.gamestate[self.selection_indice[i + 1]][2]
            self.gamestate[self.selection_indice[i]][3] += self.gamestate[self.selection_indice[i + 1]][3]
        self.selection_indice = [0]

    def expand(self, child):  # expands all the possible childs of a given node
        childs = [copy.deepcopy(child) for i in range(len(child[0]))]
        todelete_indices = []
        for i in range(len(child[0])):
            if childs[i][0][i] == 0:
                childs[i][0][i] = child[1]
                childs[i][1] = -child[1]
                childs[i][2], childs[i][3], childs[i][4], childs[i][-1] = 0, 0, 0, -1
            else:
                todelete_indices.append(i)
        self.expanded.append([result for i, result in enumerate(childs) if i not in todelete_indices])
        self.update(self.expanded)
        child[-1] = self.expanded.index(self.expanded[-1])

    def selection(self, parent): # selects the children of input (parent) with the higher UCB1 factor
        list_value = []
        for i in self.expanded[parent[-1]]:
            list_value.append(self.UCB_factor(i))
        result = self.expanded[parent[-1]][list_value.index(max(list_value))]
        for i in self.gamestate:
            if i[0] == result[0]:
                self.selection_indice.append(self.gamestate.index(i))
        self.selected.append(result)
        self.selected = self.selected[-4:]
        self.current_child = result
        return result

    def check_leaf(self): # checks if the child is a terminal node
        if self.current_child[0].count(0) == 0:
            return True

    def update(self, state): # updates all the visited states of the tree
        if len(self.gamestate) == 0:
            self.gamestate.append(state)
        else:
            for i in state[-1]:
                self.gamestate.append(i)

    def __str__(self, mode):
        return
