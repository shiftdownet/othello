
from .Decorator import Decorator

class Decorator_JudgeByPosition(Decorator):
    def _scoring(self, case):
        scoreBoard = \
            [
                [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                [0,  30, -12,   0,   1,   1,   0, -12,  30,   0],
                [0, -12, -15,  -3,  -3,  -3,  -3, -15, -12,   0],
                [0,   0,  -3,   0,  -1,  -1,   0,  -3,   0,   0],
                [0,   1,  -3,  -1,  -1,  -1,  -1,  -3,   1,   0],
                [0,   1,  -3,  -1,  -1,  -1,  -1,  -3,   1,   0],
                [0,   0,  -3,   0,  -1,  -1,   0,  -3,   0,   0],
                [0, -12, -15,  -3,  -3,  -3,  -3, -15, -12,   0],
                [0,  30, -12,   0,   1,   1,   0, -12,  30,   0],
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
