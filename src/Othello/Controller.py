
import random
import copy

from .Cell import Cell
from .Board import Board
import Agent

from termcolor import colored, cprint
import colorama
colorama.init()

class Controller():
    def __init__(self):
        self.boards = []
        self.boards.append(Board())

        self.agent = {}
        self.agent[Cell.WHITE] = self.createAgent( Cell.WHITE, int(input("white level:")) )
        self.agent[Cell.BLACK] = self.createAgent( Cell.BLACK, int(input("black level:")) )
        self.player = Cell.BLACK

    def main(self):
        passedCount = 0
        while passedCount < 2:
            print("---------------------")
            print(colored("●", "white", "on_green"), end="")
            print(self.boards[-1].whiteDisc)
            print(colored("●", "grey", "on_green"), end="")
            print(self.boards[-1].blackDisc)

            cases = self.possibleCases()

            if len(cases) != 0:
                scoringCases  = self.agent[self.player].evaluate(cases)
                print("score:",scoringCases)
                maxScoreCases = [ cases[index] for index, value in enumerate(scoringCases) if value == max(scoringCases) ]
                self.boards.append(random.choice(maxScoreCases))

                passedCount = 0

            else:
                passedCount += 1

            self.player *= -1


    def possibleCases(self):

        cases = []
        index = 0
        print("  A B C D E F G H")
        for y in range(1, 9):
            print(y, end="")
            for x in range(1, 9):
                newboard = copy.deepcopy(self.boards[-1])
                if newboard.at(x, y).put(self.player) != 0:
                    print(colored("{0:<2}".format(index), "yellow", "on_green"), end="")
                    index += 1
                    cases.append(newboard)
                else:
                    self.showCell(self.boards[-1].at(x, y).get())
            print("")
        return cases

    def showCell(self,cell):
        STR_EMPTY = "□"
        STR_BLACK = "●"
        STR_WHITE = "●"

        if cell == Cell.EMPTY:
            print(colored(STR_EMPTY, "white", "on_green"), end="")

        elif cell == Cell.BLACK:
            print(colored(STR_BLACK, "grey", "on_green"), end="")

        else:
            print(colored(STR_BLACK, "white", "on_green"), end="")

    def createAgent(self, discType, level):
        if level == 0:
            return Agent.Player(discType)

        if level >= 1:
            agent = Agent.StdAgent(discType)

        if level >= 2:
            agent = Agent.Decorator_AvoidLosingAllDisc(agent, 500)

        if level == 3:
            agent = Agent.Decorator_MaximizeOwnDisc(agent, 1)

        if level >= 4:
            agent = Agent.Decorator_JudgeByPosition(agent, 1)

        if level >= 5:
            agent = Agent.Decorator_AvoidPutOnX(agent, 100)
            agent = Agent.Decorator_AvoidPutOnRiskyC(agent, 100)
            agent = Agent.Decorator_AvoidRobbedCorner(agent, 100)
            agent = Agent.Decorator_AimAtCorner(agent,100)

        if level >= 6:
            agent = Agent.Decorator_EvaluateFlipCount(agent, 10)

        if level >= 7:
            agent = Agent.Decorator_MinimizeEnemyMoves(agent, 20)
            agent = Agent.Decorator_MaximizeOwnMoves(agent, 25)

        if level >= 8:
            agent = Agent.Decorator_MinimizeOpenness(agent, 30)

        if level >= 9:
            # agent = Agent.Decorator_EvaluateWing(agent, 10)
            pass

        if level >= 10:
            # agent = Agent.Decorator_EvaluateStoner(agent, 10)
            pass

        if level >= 11:
            # agent = Agent.Decorator_EvenOddTheory(agent, 10)
            pass

        return agent

