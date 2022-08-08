from MCTS import Game

def cycle(g):
    g.expand()
    g.random_simulation(50)
    g.UCB_factor()
    g.selection()
    g.backpropogation()

def Run_game():
    g = Game(initial_state, to_win)
    g.update(initial_state)
    while g.expandlenght != 1:
        cycle(g)
    print(g.selected)

def play(): # runs the game between the user and the computer
    return

if __name__ == '__main__':
    initial_state, to_win = [[0, 0, 0, 0, 0, 0, 0, 0], 1, 0, 0, 0], 1
    Run_game()
