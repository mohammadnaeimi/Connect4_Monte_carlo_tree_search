import random
import copy
from MCTS import Game

def Cycle(expand, number_of_total_simulations): # one Cycle: gives the expanded children, simulates them to the terminal and calculates the UCB
    for i in expand:
        g.random_simulation(i, 5)
        number_of_total_simulations += i[4]
        g.UCB_factor(i, number_of_total_simulat
                     

if __name__ == '__main__': # 0:State - 1:To_play - 2:Value - 3:Number_of_wins - 4:Number_of_visits - 5:expanded_or_not - 6:UCT_factor
    initial_state = [[0, 0, 0, 0], 1, 0, 0, 0, 0, 0]
    g = Game()
    g.update(initial_state)
    expand = g.expand(initial_state)
    number_of_total_simulations = 0
    Cycle(expand, number_of_total_simulations)
    g.update(expand)
    select = g.selection(expand)
    expand = g.expand(select)
    Cycle(expand, number_of_total_simulations)
    g.update(expand)
    select = g.selection(expand)
    expand = g.expand(select)
    Cycle(expand, number_of_total_simulations)
    g.update(expand)
    select = g.selection(expand)
    expand = g.expand(select)
    g.update(expand)
    g.backpropogation(select)
    print(g)
