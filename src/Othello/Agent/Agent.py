

from Othello.Cell import Cell
import random

class Agent():
    def __init__(self, discType):
        self.discType = discType

    def scoring(self, case ):
        return 0

    def mineDiscCount(self, case):
        return { Cell.BLACK: case.blackDisc, Cell.WHITE: case.whiteDisc }[ self.discType ]


class AgentIncreaseOwnDisc(Agent):
    def scoring(self, case):
        return self.mineDiscCount(case)



class AgentDecreaseEnemyCase(Agent):
    def scoring(self, case):
        placeableCount = 0
        for y in range(1,9):
            for x in range(1,9):
                if case.at(y,x).gettableCount( self.discType * -1 ) != 0:
                    placeableCount += 1

        return placeableCount * -1

class AgentMinOpenness(Agent):
    def scoring(self, case):

        myOpenness = 0
        enOpenness = 0
        for y in range(1,9):
            for x in range(1,9):
                if case.at(y,x).get() != Cell.EMPTY:
                    for direction in [ {"y":y,"x":x} for y in range(-1,2) for x in range(-1,2) if not (y==0 and x==0) ]:
                        if case.at(y,x).isValidRange() and case.at(y,x).offset( direction["x"], direction["y"] ).isEmpty():
                            if case.at(y,x).get() == self.discType:
                                myOpenness += 1
                            else:
                                enOpenness += 1


        return enOpenness - myOpenness


