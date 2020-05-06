

from Othello.Cell import Cell
from .Decorator import Decorator

class Decorator_MaximizeOwnDisc(Decorator):
    def _scoring(self, case):
        score = {Cell.BLACK: case.blackDisc,
                 Cell.WHITE: case.whiteDisc}[self._discType]
        return (self._rate * score) + self._agent._scoring(case)

    def _prepare(self, cases):
        self._agent._prepare(cases)
