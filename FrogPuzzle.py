class FrogPuzzle(object):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.count = 0

    def hopR(self):
        if self.initial == self.goal:
            print(f"Goal state achived with {self.count} moves.")
        else:
            index = self.initial.index(0)
            self.initial[index],self.initial[index-2] = self.initial[index-2], self.initial[index]
            print(self.initial)
            self.count += 1
            if self.initial == self.goal:
                print(f"Goal state achived with {self.count} moves.")

    def hopL(self):
        if self.initial == self.goal:
            print(f"Goal state achived with {self.count} moves.")
        else:
            index = self.initial.index(0)
            self.initial[index],self.initial[index+2] = self.initial[index+2], self.initial[index]
            print(self.initial)
            self.count += 1
            if self.initial == self.goal:
                print(f"Goal state achived with {self.count} moves.")

    def moveR(self):
        if self.initial == self.goal:
            print(f"Goal state achived with {self.count} moves.")
        else:
            index = self.initial.index(0)
            self.initial[index-1], self.initial[index] = self.initial[index], self.initial[index-1]
            print(self.initial)
            self.count += 1
            if self.initial == self.goal:
                print(f"Goal state achived with {self.count} moves.")

    def moveL(self):
        if self.initial == self.goal:
            print(f"Goal state achived with {self.count} moves.")
        else:
            index = self.initial.index(0)
            self.initial[index+1], self.initial[index] = self.initial[index], self.initial[index+1]
            print(self.initial)
            self.count += 1
            if self.initial == self.goal:
                print(f"Goal state achived with {self.count} moves.")

initial = [1,1,1,0,2,2,2]
goal = [2,2,2,0,1,1,1]

play = FrogPuzzle(initial, goal)
play.moveL()
play.hopR()
play.moveR()
play.hopL()
play.hopL()
play.moveL()
play.hopR()
play.hopR()
play.hopR()
play.moveL()
play.hopL()
play.hopL()
play.moveL()
play.hopR()
play.hopR()
play.moveL()
