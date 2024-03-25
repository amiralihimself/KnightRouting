import graphics
import numpy as np
import tkinter as tk
import time
def round_down(num, divisor):
    return num - (num%divisor)

class chessBoard:
    def __init__(self, dimension, squareSize, screenHeight, screenWidth):
        self.setText = None
        self.window = None
        self.setButton = None
        self.dimension=dimension
        self.screenwidth=screenWidth
        self.screenheight=screenHeight
        self.boardArray=np.zeros((self.dimension, self.dimension))
        self.squareSize= squareSize



    def drawBoard(self, screenTitle):
        self.window = graphics.GraphWin(screenTitle, self.screenwidth, self.screenheight)
        self.window.setBackground('lightblue')  # initializing the window's background
        x=0
        y=0
        direction=True
        for j in range(self.dimension):
            for i in range(self.dimension):
                pt1 = graphics.Point(x, y)
                pt2 = graphics.Point(x + self.squareSize, y + self.squareSize)
                rect = graphics.Rectangle(pt1, pt2)
                if direction:
                    rect.setFill("black")
                    direction = False  # making sure that two squares next to each other have different colors
                else:
                    rect.setFill("white")
                    direction = True
                rect.draw(self.window)
                x += self.squareSize
            direction = not direction
            x = 0
            y += self.squareSize
        self.setButton = graphics.Rectangle(graphics.Point(self.screenwidth-150,0),graphics.Point(self.screenwidth,50))
        self.setButton.setFill("brown")
        self.setButton.draw(self.window)
        self.setText = graphics.Text(graphics.Point(self.screenwidth-75, 25), "Set barriers")
        self.setText.setFill("orange")
        self.setText.draw(self.window)

    def setBarriers(self):
        master = tk.Tk()
        master.title("Prompt :")
        tk.Label(master, text="Please position the barriers").grid()
        tk.Button(master, text="ok!", command=master.destroy).grid()
        while True:
            mouseevent = self.window.getMouse()
            if mouseevent.x > self.squareSize*self.dimension or mouseevent.y > self.squareSize*self.dimension :
                rect1 = self.setButton.p1;
                print(rect1.x, rect1.y)
                rect2 = self.setButton.p2;
                print(rect2.x, rect2.y)
                if rect1.x < mouseevent.x < rect2.x and rect1.y < mouseevent.y < rect2.y:
                    self.setText.setText("Barriers set")
                    break
                else:
                    continue
            else:
                lower_bound = round_down(mouseevent.x, self.squareSize)
                upper_bound = round_down(mouseevent.y,self.squareSize)
                self.boardArray[int(upper_bound / self.squareSize)][int(lower_bound / self.squareSize)] = 1
                barrier = graphics.Circle(graphics.Point(lower_bound + 15, upper_bound + 15), self.squareSize/3)
                barrier.setFill("red")
                barrier.draw(self.window)



