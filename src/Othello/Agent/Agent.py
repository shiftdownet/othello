

from Othello.Cell import Cell
import random


class IAgent():
    def getScore(self):
        pass

    def scoring(self, case):
        pass


class StdAgent(IAgent):
    def __init__(self, discType):
        self._score = 0
        self._discType = discType

    def getScore(self):
        return self._score

    def scoring(self, case):
        pass


class AgentDecorator(IAgent):
    def __init__(self, agent, rate):
        self._score = 0
        self._discType = agent._discType

        self._agent = agent
        self._rate = rate

    def getScore(self):
        return self._score + self._agent._score

    def scoring(self, case):
        self._agent.scoring(case)


class MaximizeOwnDisc(AgentDecorator):
    def scoring(self, case):
        score = {Cell.BLACK: case.blackDisc,
                 Cell.WHITE: case.whiteDisc}[self._discType]
        self._score = self._rate * score
        self._agent.scoring(case)


class MinimizeOwnDisc(AgentDecorator):
    def scoring(self, case):
        score = {Cell.BLACK: case.blackDisc,
                 Cell.WHITE: case.whiteDisc}[self._discType] * -1
        self._score = self._rate * score
        self._agent.scoring(case)


class MinimizeEnemyMoves(AgentDecorator):
    def scoring(self, case):
        placeableCount = 0
        for y in range(1, 9):
            for x in range(1, 9):
                if case.at(y, x).gettableCount(self.discType * -1) != 0:
                    placeableCount += 1

        score = (placeableCount * -1)
        self._score = self._rate * score
        self._agent.scoring(case)


class MinimizeOpenness(AgentDecorator):
    def scoring(self, case):
        myOpenness = 0
        enOpenness = 0
        for y in range(1, 9):
            for x in range(1, 9):
                if case.at(y, x).get() != Cell.EMPTY:
                    for direction in [{"y": y, "x": x} for y in range(-1, 2) for x in range(-1, 2) if not (y == 0 and x == 0)]:
                        if case.at(y, x).isValidRange() and case.at(y, x).offset(direction["x"], direction["y"]).isEmpty():
                            if case.at(y, x).get() == self._discType:
                                myOpenness += 1
                            else:
                                enOpenness += 1

        score = (enOpenness - myOpenness)
        self._score = self._rate * score
        self._agent.scoring(case)


class JudgeByPosition(AgentDecorator):
    def scoring(self, case):
        scoreBoard = \
            [
                [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                [0,  30,  -5,   5,   5,   5,   5,  -5,  30,   0],
                [0,  -5, -30,   0,   0,   0,   0, -30,  -5,   0],
                [0,   5,   0,   0,   0,   0,   0,   0,   5,   0],
                [0,   5,   0,   0,   0,   0,   0,   0,   5,   0],
                [0,   5,   0,   0,   0,   0,   0,   0,   5,   0],
                [0,   5,   0,   0,   0,   0,   0,   0,   5,   0],
                [0,  -5, -30,   0,   0,   0,   0, -30,  -5,   0],
                [0,  30,  -5,   5,   5,   5,   5,  -5,  30,   0],
                [0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
            ]

        score = 0
        for y in range(1, 9):
            for x in range(1, 9):
                if case.at(y, x).get() == self._discType:
                    score += scoreBoard[y][x]

        self._score = self._rate * score
        self._agent.scoring(case)
