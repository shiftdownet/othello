from .IAgent import IAgent

class Decorator(IAgent):
    def __init__(self, agent, rate):
        self._discType = agent._discType
        self._agent = agent
        self._rate = rate

    def evaluate(self, cases):
        self._prepare( cases )

        scores = []
        for case in cases:
            scores.append(self._scoring(case))
        return scores

    def _scoring(self, case):
        self._agent._scoring(case)

    def _prepare(self, cases):
        pass