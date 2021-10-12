import os

class Node():
  def __init__(self,column,row):
    self.column = column
    self.row=row

class mazeReader():
    def __init__(self,mazeFileName):
        #Python is giving me errors based on not finding the mazes even though they're stored in the same directory.
        # This seems to fix the issue, and should make the code more portable 
        thisDirectory = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(thisDirectory, mazeFileName)
        f = open(filename,"r")
        self.mazeColumns = 0
        self.maze2DArray = []
        for line in f: #Read the maze into a 2D array one line at a time.
            self.mazeColumns = self.mazeColumns+1
            line = line.strip("\n")
            self.maze2DArray.append(line)
        #print(self.maze2DArray[0])
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

class Tile:
    def __init__(self, column, row, tileChar):
        self.column = column
        self.row = row
        self.tileChar = tileChar
        self.isGoal = False
        self.isPassable = False
        self.isStart = False
        if(tileChar != "#"):
          self.isPassable = True
        if(tileChar == "o"):
          self.isStart = True
        if(tileChar == "*"):
          self.isGoal == True
    def getXY(self):
        return self.column, self.row
    def getDistanceToGoal(self, goalNode):
        if(self.isGoal):
            return 0
        else:
          distanceToGoal = ((self.column - goalNode.column)**2 + (self.row - goalNode.row)**2)**.5
          return distanceToGoal
        
class bfsGraph:
    # Constructor
    def __init__(self):
        # empty dictionary to store graph
        self.bfsGraph = {}
    # function to add an edge to graph
    def addTile(self,u,*edges): # You can create a tile here, or add new edges to it. The number of new edges can be 0 or more. (O typically means you are adding a tile with no connections)
        if(u not in self.bfsGraph):
            self.bfsGraph[u] = [u]
        for tile in edges:
            if [tile] not in self.bfsGraph[u]:
                self.bfsGraph[u] = self.bfsGraph[u] + [tile]


        #self.bfsGraph[u].append(v)
    # Function to BFS through our maze->graph and find the Tile marked as "Goal"
    def BFS(self, s): #s is the start state S is the goal state. Goal is the tile
        # Mark all the vertices as not visited
        visited = {}
        for node in self.bfsGraph:
            visited[node] = False
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s.getXY())
            #print (s, end = " ")
            if (s.isGoal):
                print("Reached goal 2222!")
                print(s.getXY())
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.bfsGraph[s]:
                if( i.isGoal):
                    print("reached goal state!")
                    print (i.getXY())
                    break
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True        


        


mazeFile = "maze-1.txt"
maze = mazeReader(mazeFile)
#print(maze.mazeRows)
#maze.mazeToString()
maze.fromChar(maze.maze2DArray[1][2])
#print(maze.spaceToString(1,2))
#print(maze.maze2DArray)



bfs1 = bfsGraph() #Empty graph. Start by creating lone 
Tiles = [[]] * maze.mazeRows
#print(maze.mazeRows, maze.mazeColumns)
#print(Tiles[10][8])
#print(Tiles[10][10])

 ##Convert the 2D array of ints into a 2D array of tile Object
startTile = None
goalTile = None
for column in range(0,maze.mazeColumns):
  for row in range(0,maze.mazeRows):
    print(row, column, maze.maze2DArray[column][row])

    newtile = Tile(column,row,maze.maze2DArray[column][row])
    if(newtile.isStart):
      print("Found start", column, row,  maze.maze2DArray[column][row])
      startTile = newtile
    if(newtile.isGoal):
      goalTile = newtile
      print("Found goal", column, row,  maze.maze2DArray[column][row])
    bfs1.addTile(newtile)
    Tiles[row].append(newtile)

    #print(row, column)
#print(Tiles[2])

#Check adjacency of Tiles and add edges appropriately
print(Tiles[0][0].isPassable)
for row in range(0,maze.mazeRows):
  for column in range(0,maze.mazeColumns):
    currentTile = Tiles[row][column]
    if (currentTile.isPassable):
      if (column+1 < maze.mazeColumns and Tiles[row][column+1].isPassable):
        bfs1.addTile(Tiles[row][column],Tiles[row][column+1])
      if(row+1 < maze.mazeRows and Tiles[row+1][column].isPassable):
        bfs1.addTile(Tiles[row][column],Tiles[row+1][column])
    
#


print(maze.maze2DArray[1][5])
bfs1.BFS(startTile)
