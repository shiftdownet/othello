

import copy

from Othello.Agent.Agent import *
from Othello.Cell import Cell
from Othello.Board import Board


class Controller():
    def __init__(self):
        self.boards = []
        self.boards.append(Board())

        self.agent = {}
#        self.agent[Cell.WHITE] = MinimizeOpenness(StdAgent(Cell.WHITE), 1)

        self.agent[Cell.WHITE] = JudgeByPosition( MinimizeOpenness(StdAgent(Cell.WHITE), 1), 1)
        self.agent[Cell.BLACK] = StdAgent(Cell.BLACK)
#        self.agent[Cell.BLACK] = JudgeByPosition( MaximizeOwnDisc(StdAgent(Cell.BLACK), 1), 1)
        self.player = Cell.BLACK

    def main(self):
        passedCount = 0
        while passedCount < 2:
            print("------")
            self.showBoard(self.boards[-1])
            input()

            cases = self.possibleCases()

            if len(cases) != 0:
                scoringCases  = self.agent[self.player].evaluate(cases)
                print(scoringCases)
                maxScoreCases = [ cases[index] for index, value in enumerate(scoringCases) if value == max(scoringCases) ]
                self.boards.append(random.choice(maxScoreCases))

                passedCount = 0

            else:
                passedCount += 1

            self.player *= -1

        # self.showBoard(self.boards[-1])

    def possibleCases(self):
        cases = []
        for y in range(1, 9):
            for x in range(1, 9):
                newboard = copy.deepcopy(self.boards[-1])
                if newboard.at(y, x).put(self.player) != 0:
                    cases.append(newboard)
        return cases

    def showBoard(self, board):
        if self.player == Cell.BLACK:
            print(" W :", board.whiteDisc)
            print("[B ]:", board.blackDisc)
        else:
            print("[W]:", board.whiteDisc)
            print(" B :", board.blackDisc)

        for i in range(1, 9):
            for j in range(1, 9):
                print(["・", "B ", "W "][board.at(i, j).get()], end="")
            print("")
        print("")
