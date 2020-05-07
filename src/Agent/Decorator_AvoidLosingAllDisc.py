

from .Decorator import Decorator
from Othello.Cell import Cell
import copy


class Decorator_AvoidLosingAllDisc(Decorator):
    def _scoring(self, case):
        score = 0
        possibleCases = self.possibleCases(case)

        for possibleCase in possibleCases:
            numOwnDisc = {Cell.BLACK: possibleCase.blackDisc,
                          Cell.WHITE: possibleCase.whiteDisc}[self._discType]
            if numOwnDisc == 0:
                score -= 1

        return (self._rate * score) + self._agent._scoring(case)

    def _prepare(self, cases):
        self._agent._prepare(cases)


    def possibleCases(self,case):
        cases = []
        for y in range(1, 9):
            for x in range(1, 9):
                newboard = copy.deepcopy(case)
                if newboard.at(x, y).put(self._discType*-1) != 0:
                    cases.append(newboard)
        return cases
