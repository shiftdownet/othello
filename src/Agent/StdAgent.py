from .IAgent import IAgent

class StdAgent(IAgent):
    def __init__(self, discType):
        self._discType = discType

    def evaluate(self, cases):
        self._prepare( cases )

        scores = []
        for case in cases:
            scores.append(self._scoring(case))
        return scores

    def _scoring(self, case):
        return 0

    def _prepare(self, cases):
        pass
