

import copy

from Othello.Agent.Agent import *
from Othello.Cell import Cell
from Othello.Board import Board


class Controller():
    def __init__(self):
        self.boards = []
        self.boards.append( Board() )

        self.agent = {}
        self.agent[Cell.BLACK] = AgentIncreaseOwnDisc( Cell.BLACK )
        self.agent[Cell.WHITE] = AgentDecreaseEnemyCase( Cell.WHITE )
        self.player = self.agent[Cell.WHITE].discType

    def main(self):
        passedCount = 0
        while passedCount < 2:
            self.showBoard(self.boards[-1])
            input()
            cases = []
            for y in range(1,9):
                for x in range(1,9):
                    newboard = copy.deepcopy(self.boards[-1])
                    if newboard.at(y, x).put(self.player) != 0:
                        cases.append(newboard)
                
            if len(cases) != 0:
                self.boards.append( self.agent[self.player].choice( cases ) )
                passedCount = 0
            else:
                passedCount += 1

            self.player *= -1

        # self.showBoard(self.boards[-1])

    def showBoard(self, board):
        if self.player == Cell.BLACK:
            print(" ○ :", board.whiteDisc)
            print("[●]:", board.blackDisc)
        else:
            print("[○]:", board.whiteDisc)
            print(" ● :", board.blackDisc)

        for i in range(1,9):
            for j in range(1,9):
                print(["・","●","○"][board.at(i, j).get()], end="")
            print("")
        print("")

