import random
import copy
import math

class Game:

    def __init__(self, initiate): # input value is a list containing >> 0:State - 1:To_play - 2:Number_of_wins - 3:Number_of_visits - 4:UCT_factor
        self.toplay = initiate[1] # the players who's win is simulated 
        self.gamestate = [] # the states of the game which have been visited
        self.number_of_total_simulations = 0 
        self.selected = [initiate] # the nodes
        self.expandindex = 1
        self.expandlenght = 0

    def rand_child(self, child):  # this function creates a random child from the given node
        indice = [index for (index, item) in enumerate(child[0]) if item == 0]
        random_ind = random.choice(indice)
        child[0][random_ind] = child[1]
        child[1] = -child[1]
        #print(child)
        return child

    def random_simulation(self, child, number_of_simulations):
        # this function randomly simulates ''n = number_of_simulations times'' the entire game from the given node, calculates the value of terminal node and
        # returns the given node with the updated value and number of visits
        depth = child[0].count(0)
        for j in range(number_of_simulations):
            childs = [copy.deepcopy(child)]
            #childs[0][2] = 0
            for i in range(depth):
                childs.append(self.rand_child(childs[i]))
            value = self.value_policy(childs[0])[2]
            if value * self.toplay > 0:
                #child[2] += value
                child[2] += 1
            child[3] += 1
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


    def expand(self, child):  # expands all the possible childs of a given node
        childs = [copy.deepcopy(child) for i in range(len(child[0]))]
        todelete_indices = []
        for i in range(len(child[0])):
            if childs[i][0][i] == 0:
                childs[i][0][i] = child[1]
                childs[i][1] = -child[1]
                childs[i][2], childs[i][3], childs[i][4] = 0, 0, 0
            else:
                todelete_indices.append(i)
        result = [result for i, result in enumerate(childs) if i not in todelete_indices]
        self.update(result)
        self.expandlenght = len(result)
        return result

    def backpropogation(self): # updates the selected childs with the simulations
        length = len(self.gamestate)
        for i in range(self.expandindex, length):
            self.selected[0][2] += self.gamestate[i][2]
            self.selected[0][3] += self.gamestate[i][3]
        self.expandindex += self.expandlenght


    def selection(self, childs):
        list_value = []
        for i in childs:
            list_value.append(i[4])
        result = childs[list_value.index(max(list_value))]
        self.selected.append(result)
        return result

    def cycle(self, expand):
        for i in expand:
            self.random_simulation(i, 5)
            self.number_of_total_simulations += i[3]
            self.UCT_factor(i)

    def UCT_factor(self, child):
        child[4] = round((child[2] / child[3]) + math.sqrt(2) * math.sqrt(math.log(self.number_of_total_simulations) / child[3]), 2)
        return child

    def update(self, state):
        if len(self.gamestate) == 0:
            self.gamestate.append(state)
        else:
            for i in state:
                self.gamestate.append(i)

    def __str__(self, mode):
        return
