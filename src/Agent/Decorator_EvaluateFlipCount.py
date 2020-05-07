

from Othello.Cell import Cell
from .Decorator import Decorator
from .Decorator_MaximizeOwnDisc import Decorator_MaximizeOwnDisc
from .Decorator_MinimizeOwnDisc import Decorator_MinimizeOwnDisc

class Decorator_EvaluateFlipCount(Decorator):
    def _scoring(self, case):
        if self._step < 40:
            score = Decorator_MinimizeOwnDisc(self._agent, 1)._scoring(case)
        elif self._step < 60:
            score = 0
        else:
            score = Decorator_MaximizeOwnDisc(self._agent, 1)._scoring(case)

        return (self._rate * score) + self._agent._scoring(case)

    def _prepare(self, cases):
        self._agent._prepare(cases)
        self._step = self.__stepCount(cases[0])

    def __stepCount(self,case):
        step = 64
        for y in range(1,9):
            for x in range(1,9):
                if case.get() == Cell.EMPTY:
                    step -= 1
        return step
