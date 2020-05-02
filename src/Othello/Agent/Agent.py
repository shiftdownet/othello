

from Othello.Cell import Cell
import random

class Agent():
    def __init__(self, discType):
        self.discType = discType

    def choice(self, cases ):
        print("Agent")
        return random.choice( cases )

    def mineDiscCount(self, case):
        return { Cell.BLACK: case.blackDisc, Cell.WHITE: case.whiteDisc }[ self.discType ]


class AgentIncreaseOwnDisc(Agent):
    def choice(self, cases):
        print("AgentIncreaseOwnDisc")
        maxMyDisc = 0
        choisedCases = []

        for case in cases:
            if maxMyDisc < self.mineDiscCount(case):
                maxMyDisc = self.mineDiscCount(case)
        
        for case in cases:
            if maxMyDisc == self.mineDiscCount(case):
                choisedCases.append( case )

        return random.choice(choisedCases)


class AgentDecreaseEnemyCase(Agent):
    def choice(self, cases):
        print("AgentDecreaseEnemyCase")
        minPlaceableCount = 64

        for case in cases:
            placeableCount = 0
            for y in range(1,9):
                for x in range(1,9):
                    if case.at(y,x).gettableCount( self.discType * -1 ) != 0:
                        placeableCount += 1

            if minPlaceableCount > placeableCount:
                minPlaceableCount = placeableCount
                choicedCase = case
        
        return choicedCase


