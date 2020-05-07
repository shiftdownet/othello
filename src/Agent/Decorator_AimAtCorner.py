
from .Decorator import Decorator


class Decorator_AimAtCorner(Decorator):
    def _scoring(self, case):
        score = 0

        if case.at(1, 1).get() == self._discType:
            score += 1

        if case.at(1, 8).get() == self._discType:
            score += 1

        if case.at(8, 1).get() == self._discType:
            score += 1

        if case.at(8, 8).get() == self._discType:
            score += 1

        return (self._rate * score) + self._agent._scoring(case)

    def _prepare(self, cases):
        self._agent._prepare(cases)
