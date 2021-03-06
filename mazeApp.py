from tkinter import *
from tkinter import ttk
import time

from project1Current import mazeReader

class MazeApp:
    window = Tk()
    window.title('Maze')
    window.geometry("500x500")
    maze = mazeReader("maze-4.txt")
    cell_size = 30
    canvas = Canvas(window, width = cell_size*maze.mazeColumns, height = cell_size*maze.mazeRows)
    status = ttk.Label(window)
    status.place(x=100, y=10)
    itemPos = dict()

    def _init_(self):
        ttk.Button(self.window ,text="Load", command=self.create).place(x=10, y=30)
        ttk.Button(self.window, text="start", command=self.start).place(x=10, y=60)
        self.status.config(text="No Maze")
        self.window.mainloop()

    def create(self):
        if not self.maze.maze2DArray:
            return

        self.canvas.place(x=10, y=90)
        for row in range(self.maze.mazeRows):
            for col in range(self.maze.mazeColumns):
                curfield = self.maze.maze2DArray[row][col]
                if curfield == '.':
                    color = 'White'
                elif curfield == '#':
                    color = 'black'
                elif curfield == 'o':
                    color = 'red'
                elif curfield == '*':
                    color = 'green'

                self.draw(row, col, color)
        self.status.config(text="Maze Loaded")
 
    def draw(self, row, col, color):
        cell_size = self.cell_size
        x1 = col*cell_size
        y1 = row*cell_size
        x2 = x1+cell_size
        y2 = y1+cell_size
        curcell = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.itemPos[str(row)+str(col)] = curcell

    def start(self):
        self.status.config(text="Solution in progress")

        bfsPath = self.maze.aStarV2() 
        if (len(bfsPath) < 1):
            self.status.config(text="Solution complete: exit not reachable")
            return
        else:
            finalPath = bfsPath[len(bfsPath)-1]

        for cell in bfsPath:
            row = cell[0]
            col = cell[1]
            curcell = self.itemPos[str(row)+str(col)]
            self.window.update()
            time.sleep(1)
            self.canvas.itemconfig(curcell, fill="grey")
        self.status.config(text="Solution complete: exit reachable at {0},{1} in {2} moves".format(finalPath[0], finalPath[1], len(bfsPath)))
        
maze = MazeApp()
maze._init_()
