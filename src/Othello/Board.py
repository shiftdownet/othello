
from Othello.Cell import Cell

class Board():
    def __init__(self):
        self.__cells = [ [ Cell() for i in range(8 + 2) ] for j in range(8 + 2) ] # It includes sentinel
        self.__x = 0
        self.__y = 0
        self.__offsetX = 0
        self.__offsetY = 0
        self.at(4,4).access().put(Cell.BLACK)
        self.at(4,5).access().put(Cell.WHITE)
        self.at(5,4).access().put(Cell.WHITE)
        self.at(5,5).access().put(Cell.BLACK)

        self.blackDisc = 0
        self.whiteDisc = 0
        self.count()

    def at(self, y, x):
        self.__offsetX = 0
        self.__offsetY = 0
        self.__x = x
        self.__y = y
        return self

    def offset(self, y, x):
        self.__offsetX += x
        self.__offsetY += y
        return self

    def access(self):
        y = self.__y + self.__offsetY
        x = self.__x + self.__offsetX
        self.__offsetX = 0
        self.__offsetY = 0
        return self.__cells[y][x]

    def isValidRange(self):
        y = self.__y + self.__offsetY
        x = self.__x + self.__offsetX
        return True if ( 1 <= x <= 8) and ( 1 <= y <= 8) else False

    def put(self, discType):
        totalFlipCount = 0

        # Position is valid and there is no disc yet.
        if self.isValidRange() and self.isEmpty():

            # Check each direction.
            for direction in [ {"y":y,"x":x} for y in range(-1,2) for x in range(-1,2) if not (y==0 and x==0) ]:

                # There are reverse side discs.
                laneFlipCount = 0
                while self.offset( direction["y"] * (laneFlipCount+1),
                                   direction["x"] * (laneFlipCount+1) ).isBackOf(discType):
                    laneFlipCount += 1

                # At least one.
                if laneFlipCount != 0:

                    # Finally, there is the same disc as owns.
                    if self.offset( direction["y"] * (laneFlipCount+1),
                                    direction["x"] * (laneFlipCount+1) ).isSameAs(discType):
                        totalFlipCount += laneFlipCount

                        # actually flip
                        while laneFlipCount > 0:
                            laneFlipCount -= 1
                            self.offset( direction["y"] * (laneFlipCount+1),
                                         direction["x"] * (laneFlipCount+1) ).flip()

                        # put a disc
                        self.access().put(discType)

                        self.count()

        return totalFlipCount

    def gettableCount(self, discType):
        totalFlipCount = 0

        # Position is valid and there is no disc yet.
        if self.isValidRange() and self.isEmpty():

            # Check each direction.
            for direction in [ {"y":y,"x":x} for y in range(-1,2) for x in range(-1,2) if not (y==0 and x==0) ]:

                # There are reverse side discs.
                laneFlipCount = 0
                while self.offset( direction["y"] * (laneFlipCount+1),
                                   direction["x"] * (laneFlipCount+1) ).isBackOf(discType):
                    laneFlipCount += 1

                # At least one.
                if laneFlipCount != 0:

                    # Finally, there is the same disc as owns.
                    if self.offset( direction["y"] * (laneFlipCount+1),
                                    direction["x"] * (laneFlipCount+1) ).isSameAs(discType):
                        totalFlipCount += laneFlipCount

        return totalFlipCount


    def flip(self):
        self.access().flip()

    def get(self):
        return self.access().get()

    def isEmpty(self):
        return self.access().isEmpty()

    def isSameAs(self, discType):
        return self.access().isSameAs(discType)

    def isBackOf(self, discType):
        return self.access().isBackOf(discType)

    def count(self):
        r = [0,0,0]
        for lane in self.__cells:
            for cell in lane:
                r[ cell.get() ] += 1

        self.blackDisc = r[Cell.BLACK]
        self.whiteDisc = r[Cell.WHITE]

