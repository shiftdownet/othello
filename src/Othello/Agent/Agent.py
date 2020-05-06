

from Othello.Cell import Cell
import random


class IAgent():
    def evaluate(self, cases):
        pass

    def _scoring(self, case):
        pass


class StdAgent(IAgent):
    def __init__(self, discType):
        self._discType = discType

    def evaluate(self, cases):
        scores = []
        for case in cases:
            scores.append(self._scoring(case))
        return scores

    def _scoring(self, case):
        return 0


class AgentDecorator(IAgent):
    def __init__(self, agent, rate):
        self._discType = agent._discType
        self._agent = agent
        self._rate = rate

    def evaluate(self, cases):
        scores = []
        for case in cases:
            scores.append(self._scoring(case))
        return scores

    def _scoring(self, case):
        self._agent._scoring(case)


class ManualInput(AgentDecorator):
    def evaluate(self, cases):
        scores = []
        for case in cases:
            scores.append(self._scoring(case))
        return scores


class MaximizeOwnDisc(AgentDecorator):
    def _scoring(self, case):
        score = {Cell.BLACK: case.blackDisc,
                 Cell.WHITE: case.whiteDisc}[self._discType]
        return (self._rate * score) + self._agent._scoring(case)


class MinimizeOwnDisc(AgentDecorator):
    def _scoring(self, case):
        score = {Cell.BLACK: case.blackDisc,
                 Cell.WHITE: case.whiteDisc}[self._discType] * -1
        return (self._rate * score) + self._agent._scoring(case)


class MinimizeEnemyMoves(AgentDecorator):
    def _scoring(self, case):
        placeableCount = 0
        for y in range(1, 9):
            for x in range(1, 9):
                if case.at(y, x).gettableCount(self.discType * -1) != 0:
                    placeableCount += 1

        score = (placeableCount * -1)

        return (self._rate * score) + self._agent._scoring(case)


class MinimizeOpenness(AgentDecorator):
    def _scoring(self, case):
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
        return (self._rate * score) + self._agent._scoring(case)


class JudgeByPosition(AgentDecorator):
    def _scoring(self, case):
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

        return (self._rate * score) + self._agent._scoring(case)
