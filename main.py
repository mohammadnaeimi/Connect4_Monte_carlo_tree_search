import random
import copy
from MCTS import Game


def run(g):
    g.update(initial_state)
    expand = g.expand(initial_state)
    g.cycle(expand)
    g.backpropogation()
    select = g.selection(expand)
    expand = g.expand(select)
    g.cycle(expand)
    g.backpropogation()
    select = g.selection(expand)
    print(g.gamestate)
    print(g.selected)
    print(g.expandindex)
    print(g.expandlenght)
                     

if __name__ == '__main__':
    g = Game(initial_state)
    run(g)
