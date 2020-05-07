
from .Decorator import Decorator


class Decorator_AvoidPutOnX(Decorator):
    def _scoring(self, case):
        score = 0

        if case.at(2, 2).get() == self._discType:
            score -= 1

        if case.at(2, 7).get() == self._discType:
            score -= 1

        if case.at(7, 2).get() == self._discType:
            score -= 1

        if case.at(7, 7).get() == self._discType:
            score -= 1

        return (self._rate * score) + self._agent._scoring(case)

    def _prepare(self, cases):
        self._agent._prepare(cases)
