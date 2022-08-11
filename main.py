from MCTS import Game

initial_state = [[-1, 1, 1, -1, -1, 1, 1, 0], -1, 0, 0, 0, -1]
g = Game(initial_state, -1)


def cycle():
    for i in range(10):
        iteration(initial_state)

    selection = g.expanded[0]
    list_value = []
    for i in selection:
        list_value.append(i[4])
    return selection[list_value.index(max(list_value))]

def iteration(parent):
    if parent[-1] == -1:
        g.expand(parent)
        g.selection(parent)
        g.rollout(100)
        g.backpropogation()
    else:
        g.selection(parent)
        if g.current_child[2] == 0:
            g.rollout(100)
            g.backpropogation()
        else:
            g.iteration(g.current_child)

def game_play(): # runs the game between the user and the computer

    return


if __name__ == '__main__':
    print(cycle())
