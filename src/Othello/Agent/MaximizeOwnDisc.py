

from Othello.Cell import Cell
from .AgentDecorator import AgentDecorator

class MaximizeOwnDisc(AgentDecorator):
    def _scoring(self, case):
        score = {Cell.BLACK: case.blackDisc,
                 Cell.WHITE: case.whiteDisc}[self._discType]
        return (self._rate * score) + self._agent._scoring(case)

