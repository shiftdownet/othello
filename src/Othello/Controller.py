

import copy

from Othello.Agent.Agent import *
from Othello.Cell import Cell
from Othello.Board import Board


class Controller():
    def __init__(self):
        self.boards = []
        self.boards.append( Board() )

        self.agent = {}
        self.agent[Cell.BLACK] = AgentMinOpenness( Cell.BLACK )
        self.agent[Cell.WHITE] = AgentDecreaseEnemyCase( Cell.WHITE )
        self.player = self.agent[Cell.WHITE].discType

    def main(self):
        passedCount = 0
        while passedCount < 2:
            print("------")
            self.showBoard(self.boards[-1])
            input()
            cases = []
            for y in range(1,9):
                for x in range(1,9):
                    newboard = copy.deepcopy(self.boards[-1])
                    if newboard.at(y, x).put(self.player) != 0:
                        cases.append(newboard)
                
            if len(cases) != 0:
                maxScore = -65535
                scoingCases = []
                for case in cases:
                    score = self.agent[self.player].scoring( case )
                    scoingCases.append({"score":score, "case":case })
                    if maxScore < score:
                        maxScore = score
                
                maxScoreCases = [ case["case"] for case in scoingCases if maxScore == case["score"] ]

                self.boards.append( random.choice( maxScoreCases ) )
                passedCount = 0


            else:
                passedCount += 1

            self.player *= -1

        # self.showBoard(self.boards[-1])

    def showBoard(self, board):
        if self.player == Cell.BLACK:
            print(" W :", board.whiteDisc)
            print("[B ]:", board.blackDisc)
        else:
            print("[W]:", board.whiteDisc)
            print(" B :", board.blackDisc)

        for i in range(1,9):
            for j in range(1,9):
                print(["・","B ","W "][board.at(i, j).get()], end="")
            print("")
        print("")

