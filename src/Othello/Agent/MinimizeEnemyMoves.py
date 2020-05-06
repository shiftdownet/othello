
from .AgentDecorator import AgentDecorator

class MinimizeEnemyMoves(AgentDecorator):
    def _scoring(self, case):
        placeableCount = 0
        for y in range(1, 9):
            for x in range(1, 9):
                if case.at(y, x).gettableCount(self.discType * -1) != 0:
                    placeableCount += 1

        score = (placeableCount * -1)

        return (self._rate * score) + self._agent._scoring(case)


