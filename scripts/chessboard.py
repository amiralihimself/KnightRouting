import graphics
import numpy as np
import time
class chessboard:
    def __init__(self, dimension, screenHeight, screenWidth):
        self.dimension=dimension
        self.screenwidth=screenWidth
        self.screenheight=screenHeight
        self.boardArray=np.zeros((self.dimension, self.dimension))

    def drawBoard(self, screenTitle):
        window = graphics.GraphWin(screenTitle, self.screenwidth, self.screenheight)
        window.setBackground('lightblue')  # initializing the window's background
        for j in range(self.dimension):
            for i in range(self.dimension):
                pt1 = graphics.Point(x, y)
                pt2 = graphics.Point(x + size, y + size)
                rect = Rectangle(pt1, pt2)
                if direction:
                    rect.setFill("black")
                    direction = False  # making sure that two squares next to each other have different colors
                else:
                    rect.setFill("white")
                    direction = True
                rect.draw(win)
                x += size
            direction = not direction
            x = x_start
            y += size


