import os
class mazeReader():
    def __init__(self,mazeFileName):
        #Python is giving me errors based on not finding the mazes even though they're stored in the same directory.
        # This seems to fix the issue, and should make the code more portable 
        thisDirectory = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(thisDirectory, mazeFileName)
        f = open(filename,"r")
        self.mazeColumns = 0
        self.maze2DArray = []
        for line in f:
            self.mazeColumns = self.mazeColumns+1
            self.maze2DArray.append(line)
        self.mazeRows = len(self.maze2DArray[0]) #The maze rows are all the same length. We can determine its size just from the first line.

    def mazeToString(self):
        #print("Printing maze")
        for i in range(self.mazeColumns):
            print(self.maze2DArray[i], end ="")
        print()
    def spaceToString(self, column, row):
        return self.maze2DArray[row][column]
    def fromChar(self,a):
        if(a == "."):
            print("Open space")
        elif(a == "o"):
            print("Start space")
        elif (a == "#"):
            print("Wall space")
        elif(a == "*"):
            print("Goal space")
        else:
            print("Invalid space.")

            


        


mazeFile = "maze-1.txt"
maze = mazeReader(mazeFile)
#print(maze.mazeRows)
maze.mazeToString()
maze.fromChar(maze.maze2DArray[1][2])
print(maze.spaceToString(1,2))