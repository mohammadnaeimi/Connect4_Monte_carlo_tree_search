import random
import copy
from MCTS import Game


if __name__ == '__main__':
    initial_state = [[0, 0, 0, 0, 0, 0, 0, 0], 1, 0, 0, 0, 0, 0]
    g = Game()
    expand = g.expand(initial_state)
    for i in range(10):
        select = g.selection(expand)
        randsim = g.random_simulation(select, 5)
        ufac = g.UCT_factor(randsim)
    g.update(ufac)
    print(g)
