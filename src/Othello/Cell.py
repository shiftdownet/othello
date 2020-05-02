

class Cell():
    EMPTY = 0
    BLACK = 1
    WHITE = BLACK * -1

    def __init__(self):
        self.__value = self.EMPTY
 
    def put(self, discType):
        self.__value = discType \
            if discType in { self.BLACK, self.WHITE } else self.__value

    def get(self):
        return self.__value

    def flip(self):
        self.__value *= -1

    def isEmpty(self):
        return self.__value == self.EMPTY

    def isSameAs(self, discType):
        return self.__value == discType

    def isBackOf(self, discType):
        return self.__value == discType * -1

