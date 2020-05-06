from .IAgent import IAgent

class Player(IAgent):
    def __init__(self, discType):
        self._discType = discType

    def evaluate(self, cases):
        self._prepare( cases )

        scores = [ 0 for case in cases ]

        scores[ int(input('> ')) ] = 1

        return scores

    def _scoring(self, case):
        return 0

    def _prepare(self, cases):
        pass
