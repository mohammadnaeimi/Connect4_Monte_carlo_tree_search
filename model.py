from MCTS import Game

class model():
    def __init__(self):
        self.board = initial_state

    def move(self, choose):
        move = int(input('your move...'))
        if self.board[0][move] == 0:
            self.board[0][move] = choose
            self.board[1] = -choose
        else:
            print('invalid move, think again...')
            move(choose)

    def cycle(self):
        for i in range(10):
            self.iteration(self.board)

        selection = g.expanded[0]
        list_value = []
        for i in selection:
            list_value.append(i[4])
        self.board = selection[list_value.index(max(list_value))]

    def iteration(self, parent):
        if g.check_leaf() is True:
            return
        else:
            if g.is_expanded(parent) is False:
                g.expand(parent)
                g.selection(parent)
                g.rollout(500)
                g.backpropogation()
            else:
                g.selection(parent)
                if g.is_expanded(g.current_child) is False:
                    g.rollout(500)
                    g.backpropogation()
                else:
                    self.iteration(g.current_child)

    def game_play(self):
        print(self.board)


    def __str__(self, mode):
        return
