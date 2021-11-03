from tkinter import *
from tkinter import ttk
import time
import os
from os.path import exists

from project1Current import mazeReader

class MazeApp:
    window = Tk()
    window.title('Maze')
    window.geometry("1000x1000")
    currentMaze = "maze-1.txt"
    mazeFile = ttk.Entry(window, width = 30)
    mazeFile.place(x=90,y=30)

    maze = mazeReader(currentMaze)
    cell_size = 5 #Assume the maze is giant.
    canvas = Canvas(window, width = cell_size*maze.mazeColumns, height = cell_size*maze.mazeRows)
    status = ttk.Label(window)
    status.place(x=100, y=10)
    itemPos = dict()
    running = False
    index = 0

    def _init_(self):
        global index 
        index = 0
        global running
        running = False
        ttk.Button(self.window ,text="Load", command=self.create).place(x=10, y=30)
        ttk.Button(self.window ,text="Step", command=self.step).place(x=10, y=90)
        ttk.Button(self.window, text="Start Animation", command=self.start).place(x=10, y=60)
        ttk.Button(self.window, text="Stop Animation", command=self.stop).place(x=110, y=60)
        self.status.config(text="No Maze")
        self.window.mainloop()

    def create(self):
        global running
        global index
       # self.canvas.place(x=10, y=120)
       # for row in range(50):
     #      for col in range(50):
        #        self.draw(row, col, 'black')

                
        thisDirectory = os.path.dirname(os.path.abspath(__file__))
        newFileName =  os.path.join(thisDirectory, self.mazeFile.get())
        if(self.mazeFile.get() != self.currentMaze and os.path.isfile(newFileName)):
            try:
                self.currentMaze = self.mazeFile.get()
                self.maze = mazeReader(self.mazeFile.get())
                self.canvas.delete("all")
                self.canvas = Canvas(self.window, width = self.cell_size*self.maze.mazeColumns, height = self.cell_size*self.maze.mazeRows)
                self.itemPos = dict()
                global index
                index = 0
                running = False
                self.status.config(text="new Maze Loaded: " + self.mazeFile.get() )

            except:
                self.status.config(text="Invalid maze loaded")

        if not self.maze.maze2DArray:
            return

        self.canvas.place(x=10, y=120)
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
        index = 0
        self.status.config(text="Maze Loaded")
    
    def stop(self):
        global running
        running = False
        global index 
        print("Stopped at:", index)
    def step(self):
        global running
        global index
        
        if(running == False):
            bfsPath = self.maze.aStarV2() 
            if(len(bfsPath) > 0):
                finalPath = bfsPath[len(bfsPath)-1]
            if ( index < len(bfsPath) ):
                row = bfsPath[index][0]
                col = bfsPath[index][1]
                #print("row"  , row , "col" ,col)
                #curcell = self.itemPos[str(row)+str(col)]
                self.draw(row, col, "blue")
                self.window.update()
                #self.canvas.itemconfig(curcell, fill="blue")
                index = index+1
                if(index == len(bfsPath)):
                    index = 0
                    isGoal = self.maze.mazeNodes[finalPath[0], finalPath[1]].isGoal
                    if(isGoal):
                        self.status.config(text="Solution complete: exit reachable at {0},{1} in {2} moves".format(finalPath[0], finalPath[1], len(bfsPath)))
                    else:
                        self.status.config(text="Solution complete: Exit not reachable.")
        else:
            print("Cannot step while animation is running.")


 
    def draw(self, row, col, color):
        cell_size = self.cell_size
        x1 = col*cell_size
        y1 = row*cell_size
        x2 = x1+cell_size
        y2 = y1+cell_size
        curcell = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.itemPos[str(row)+str(col)] = curcell

    def start(self):
        global running
        global index
        running = True
        self.status.config(text="Solution in progress")
        bfsPath = self.maze.aStarV2() 
       # for i in range(0,50):
            #print("row"  , bfsPath[index-10+i][0] , "col" ,bfsPath[index-10+i][1] )
        if (len(bfsPath) < 1):
            self.status.config(text="Solution complete: exit not reachable")
            return
        else:
            finalPath = bfsPath[len(bfsPath)-1]
        if(index !=0):
            for i in range(0, index):
                row = bfsPath[i][0]
                col = bfsPath[i][1]

                #curcell = self.itemPos[str(row)+str(col)]
                self.window.update()
                self.draw(row, col, "blue")
                self.window.update()
                #self.canvas.itemconfig(curcell, fill="blue")
        while (index < len(bfsPath) and running):

            row = bfsPath[index][0]
            col = bfsPath[index][1]
            print("row"  , row , "col" ,col)
            
            #curcell = self.itemPos[str(row)+str(col)]
            timerTime = 1/ self.maze.mazeColumns
            #print("Timer time" , timerTime)
            time.sleep(timerTime)
            self.draw(row, col, "blue")
            self.window.update()
            #self.canvas.itemconfig(curcell, fill="blue")
            index = index+1
        if(index == len(bfsPath)):
                index = 0
                isGoal = self.maze.mazeNodes[finalPath[0], finalPath[1]].isGoal
                if(isGoal):
                    self.status.config(text="Solution complete: exit reachable at {0},{1} in {2} moves".format(finalPath[0], finalPath[1], len(bfsPath)))
                else:
                        self.status.config(text="Solution complete: Exit not reachable.")
        

            
maze = MazeApp()
maze._init_()
