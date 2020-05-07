
from .Decorator import Decorator
from Othello.Cell import Cell

class Decorator_AvoidPutOnRiskyC(Decorator):
    def _scoring(self, case):
        score = 0

        lanes = []
        lanes.append( [ case.at(1, i).get() for i in range(0,10) ] )
        lanes.append( [ case.at(8, i).get() for i in range(0,10) ] )
        lanes.append( [ case.at(i, 1).get() for i in range(0,10) ] )
        lanes.append( [ case.at(i, 8).get() for i in range(0,10) ] )

        for lane in lanes:
            score += self.__evaluateLane(lane)
            score += self.__evaluateLane(lane[::-1])

        return (self._rate * score) + self._agent._scoring(case)

    def __evaluateLane(self, lane):
        # -: Empty
        # M: Me
        # E: Enemy

        self._index = 1
        
        if self.nextCellIs(lane, Cell.EMPTY):                                           # -
            if self.nextCellIs(lane, self._discType ):                                  # -  M
                while self.nextCellIs(lane, self._discType ):                           # -  M+
                    pass

                if self.nextCellIs(lane, Cell.EMPTY):                                   # -  M+ -
                    if self.nextCellIs(lane, self._discType ):                          # -  M+ -  M
                        while self.nextCellIs(lane, self._discType):                    # -  M+ -  M+
                            pass
                        if self.nextCellIs(lane, Cell.EMPTY ):                         # -  M+ -  M+  -
                            return -1

                    elif self.nextCellIs(lane, self._discType * -1):                    # -  M+ -  E
                        while self.nextCellIs(lane, self._discType * -1):               # -  M+ -  E+
                            pass

                        if self.nextCellIs(lane, self._discType ):                      # -  M+ -  E+  M
                            return -1

                        if self.nextCellIs(lane, Cell.EMPTY):                           # -  M+ -  E+  -
                            if self.nextCellIs(lane, self._discType * -1):              # -  M+ -  E+  - E
                                return -1

                    elif self.nextCellIs(lane, Cell.EMPTY):                             # -  M+ -  -
                        if self.nextCellIs(lane, Cell.EMPTY):                           # -  M+ -  -  -
                            if self.nextCellIs(lane, self._discType * -1):              # -  M+ -  -  - E
                                return -1
                            if self.nextCellIs(lane, Cell.EMPTY):                       # -  M+ -  -  - -
                                return -1

        return 0
    
    def nextCellIs( self, lane, discType ):
        if self._index > 8:
            return False

        if lane[self._index] == discType:
            self._index +=1
            return True

        return False

    def _prepare(self, cases):
        self._agent._prepare(cases)
