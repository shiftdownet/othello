
from Othello.Cell import Cell

class Board():
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    
    SENTINEL_SIZE = 1
    BOARD_SIZE    = 8 + SENTINEL_SIZE * 2
    BOARD_MIN = 1
    BOARD_MAX = 8

    def __init__(self):
        self.__cells = [ [ Cell() for i in range( Board.BOARD_SIZE ) ] for j in range( Board.BOARD_SIZE ) ] # It includes sentinel
        self.__x = 0
        self.__y = 0
        self.__offsetX = 0
        self.__offsetY = 0
        self.at(Board.D,4).access().put(Cell.BLACK)
        self.at(Board.D,5).access().put(Cell.WHITE)
        self.at(Board.E,4).access().put(Cell.WHITE)
        self.at(Board.E,5).access().put(Cell.BLACK)

        self.blackDisc = 0
        self.whiteDisc = 0
        self.count()

    def at(self, x, y):
        self.__offsetX = 0
        self.__offsetY = 0
        self.__x = x
        self.__y = y
        return self

    def offset(self, x, y):
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
        return True if ( Board.BOARD_MIN <= x <= Board.BOARD_MAX ) and ( Board.BOARD_MIN <= y <= Board.BOARD_MAX ) else False

    def put(self, discType):
        totalFlipCount = 0

        # Position is valid and there is no disc yet.
        if self.isValidRange() and self.isEmpty():

            # Check each direction.
            for direction in [ {"y":y,"x":x} for y in range(-1,2) for x in range(-1,2) if not (y==0 and x==0) ]:

                # There are reverse side discs.
                laneFlipCount = 0
                while self.offset( direction["x"] * (laneFlipCount+1),
                                   direction["y"] * (laneFlipCount+1) ).isBackOf(discType):
                    laneFlipCount += 1

                # At least one.
                if laneFlipCount != 0:

                    # Finally, there is the same disc as owns.
                    if self.offset( direction["x"] * (laneFlipCount+1),
                                    direction["y"] * (laneFlipCount+1) ).isSameAs(discType):
                        totalFlipCount += laneFlipCount

                        # actually flip
                        while laneFlipCount > 0:
                            laneFlipCount -= 1
                            self.offset( direction["x"] * (laneFlipCount+1),
                                         direction["y"] * (laneFlipCount+1) ).flip()

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
                while self.offset( direction["x"] * (laneFlipCount+1),
                                   direction["y"] * (laneFlipCount+1) ).isBackOf(discType):
                    laneFlipCount += 1

                # At least one.
                if laneFlipCount != 0:

                    # Finally, there is the same disc as owns.
                    if self.offset( direction["x"] * (laneFlipCount+1),
                                    direction["y"] * (laneFlipCount+1) ).isSameAs(discType):
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

