

import copy

from Othello.Agent.Agent import *
from Othello.Cell import Cell
from Othello.Board import Board


class Controller():
    def __init__(self):
        self.boards = []
        self.boards.append( Board() )

        self.agent = {}
        self.agent[Cell.WHITE] = JudgeByPosition( MinimizeOpenness( StdAgent(Cell.WHITE), 1 ), 1 )
        self.agent[Cell.BLACK] = JudgeByPosition( MaximizeOwnDisc( StdAgent(Cell.BLACK), 1 ), 1 )
#        self.agent[Cell.BLACK] = MaximizeOwnDisc( StdAgent(Cell.BLACK), 1 )
#        self.agent[Cell.BLACK] = StdAgent(Cell.BLACK)
        self.player = Cell.BLACK

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
                    self.agent[self.player].scoring( case )
                    score = self.agent[self.player].getScore()
                    #print(score)
                    scoingCases.append({"score":score, "case":case })
                    if maxScore < score:
                        maxScore = score
                if 0:
                    print("### start ###")
                    for case in scoingCases:
                        print("score:", case["score"])
                        self.showBoard(case["case"])
                    print("### end ###")

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

