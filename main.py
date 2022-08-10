from MCTS import Game

def cycle(child, game):
    depth = child[0].count(0)
    for i in range(depth):
        game.selection(child)
        game.rollout(5, game.selected[-1])
        game.backpropogation()
    return


def run(): # runs the game between the user and the computer
    initial_state, to_win = [[0, 0, 0, 0, 0, 0, 0, 0], 1, 0, 0, 0, -1], -1
    g = Game(initial_state, to_win)
    while g.check_leaf() is not True:
        g.expand(g.current_child)
        cycle(g.current_child, g)
        g.selection(g.current_child)

    print(g.gamestate)
    print(g.expanded)
    print(g.selected)
    print(g.current_child)


if __name__ == '__main__':
    run()

