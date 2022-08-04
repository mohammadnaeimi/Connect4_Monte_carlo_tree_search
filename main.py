from MCTS import Game



def cycle(g):
    g.expand()
    expand = g.expanded
    for i in expand:
        g.random_simulation(i, 50)
        g.number_of_total_simulations += i[3]
        g.UCB_factor(i)
    g.selection(expand)
    g.backpropogation()

def Run_game():
    g = Game(initial_state)
    while g.expandlenght != 1:
        cycle(g)
    print(g.gamestate)


if __name__ == '__main__':
    initial_state = [[0, 0, 0, 0, 0, 0, 0, 0], -1, 0, 0, 0]
    Run_game()
