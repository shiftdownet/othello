
from .Decorator import Decorator

class Decorator_JudgeByPosition(Decorator):
    def _scoring(self, case):
        scoreBoard = \
            [
                [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                [0,  30,  -5,   1,   1,   1,   1,  -5,  30,   0],
                [0,  -5, -30,   0,   0,   0,   0, -30,  -5,   0],
                [0,   1,   0,   0,   0,   0,   0,   0,   1,   0],
                [0,   1,   0,   0,   0,   0,   0,   0,   1,   0],
                [0,   1,   0,   0,   0,   0,   0,   0,   1,   0],
                [0,   1,   0,   0,   0,   0,   0,   0,   1,   0],
                [0,  -5, -30,   0,   0,   0,   0, -30,  -5,   0],
                [0,  30,  -5,   1,   1,   1,   1,  -5,  30,   0],
                [0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
            ]

        score = 0
        for y in range(1, 9):
            for x in range(1, 9):
                if case.at(y, x).get() == self._discType:
                    score += scoreBoard[y][x]

        return (self._rate * score) + self._agent._scoring(case)

    def _prepare(self, cases):
        self._agent._prepare(cases)
