
from .AgentDecorator import AgentDecorator

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
