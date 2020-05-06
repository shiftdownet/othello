
from Othello.Cell import Cell
from .Decorator import Decorator

class Decorator_MinimizeOpenness(Decorator):
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

    def _prepare(self, cases):
        self._agent._prepare(cases)
