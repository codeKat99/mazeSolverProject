import os
from collections import deque


# A simple implementation of Priority Queue
# using Queue.
class minPriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i].getHeuristic() < self.queue[min].getHeuristic():
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()
  

class Node:
    def __init__(self, row,column, maze):
        self.row = row
        #self.gn =
        self.column = column
        self.char = maze.spaceToString(self.row,self.column)
        self.maze = maze
        #print(self.char=="o")
        if(self.char == "#"):
            self.isPassable = False
        else: self.isPassable = True
        if(self.char == "o"):
            #print("Is start")
            self.isStart = True
        else: self.isStart = False
        if(self.char == "*"):
            self.isGoal = True
        else: self.isGoal = False
        if(self.isStart):
            self.pathCost = 0
        ## This area of the Node class will serve as the heuristic for the A* search. 
        ## IT can be ignored for BFS and DFS, however for 
        if(self.isGoal):
            self.distanceToGoal=0
        else:
            distanceToGoal = 999
            for goal in maze.goals:
                tempDist = ((column - goal[1])**2 + (row - goal[0])**2)**.5
                if (tempDist < distanceToGoal):
                    self.distanceToGoal = tempDist
        """ if(self.isStart):
            self.gn = 0
        else
            self.gn = maze.start """
    def getChildren(self):
        children = []
        #print("Get Children")
        #Check if we have a child right of us
        #print(self.maze.mazeNodes[self.row,self.column+1].isPassable)
        #print(self.maze.mazeNodes[self.row+1,self.column].isPassable)
        #print(self.maze.mazeNodes[self.row,self.column-1].isPassable)
        if(self.column+1 < self.maze.mazeColumns and self.maze.mazeNodes[self.row,self.column+1].isPassable):
            #print("Right")
            children.append(self.maze.mazeNodes[self.row,self.column+1]) 
        # Check if we have a child below us
        if(self.row+1 < self.maze.mazeRows and self.maze.mazeNodes[self.row+1,self.column].isPassable):
            #print("Below")
            children.append(self.maze.mazeNodes[self.row+1,self.column])
        #Check if we have a child left of us
        if(self.column-1 > 0 and self.maze.mazeNodes[self.row,self.column-1].isPassable):
            #print("Left")
            children.append(self.maze.mazeNodes[self.row,self.column-1])
        #Check if we have a child above us
        if(self.row-1 > 0 and self.maze.mazeNodes[self.row-1,self.column].isPassable):
            #print("Above")
            children.append(self.maze.mazeNodes[self.row-1,self.column])
        for i in range(len(children)):
            children[i].setPathCost(self.pathCost+1)
        return children
    def printXY(self):
        print("Row, Column:", self.row, ",", self.column, end="\n")
    def setPathCost(self, pathCost):
        self.pathCost = pathCost
    def incrementPathCost(self):
        self.pathCost = self.pathCost+1
    def getHeuristic(self):
        fn = self.pathCost + self.distanceToGoal #pathcost = gn. Cost to get here. distanceToGoal is hn. 
        #The distanceToGoal method might underestimate. But it cannot overestimate. It will fine the Straight Line Distance to the goal.
        return fn


# class mazeBFS():
#     def __init__(self,maze):
#         self.BFS(maze)
#
#     def BFS(self,maze):
#         print("Beginning BFS")
#         node = maze.startNode
#         if(node.isGoal):
#             return node
#         frontier = []
#         frontier.append(node)
#         visited = {}
#         visited[node] = True
#         while (frontier[0]!=None):
#             currentNode = frontier.pop(0)
#             for child in currentNode.getChildren:
#                 if(child.isGoal):
#                     return child
#                 if (visited[child]!=True):
#                     visited[child]=True
#                     frontier.append(child)
#         return "Failed"





class mazeReader():
    def __init__(self,mazeFileName):
        #Python is giving me errors based on not finding the mazes even though they're stored in the same directory.
        # This seems to fix the issue, and should make the code more portable 
        thisDirectory = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(thisDirectory, mazeFileName)
        f = open(filename,"r")
        self.mazeRows = 0
        self.maze2DArray = []
        
        self.goals = []
        for line in f: #Read the maze into a 2D array one line at a time.
            self.mazeRows = self.mazeRows+1
            line = line.strip("\n")
            self.maze2DArray.append(line)
        self.mazeColumns = len(self.maze2DArray[0]) #The maze columns are all the same length. We can determine its size just from the first line.
        #print("Maze rows:", self.mazeRows, "Maze cols:", self.mazeColumns)
        #print(self.maze2DArray[0])

        #Find all the goal Nodes
        for row in range(self.mazeRows):
            for column in range(self.mazeColumns):
                #print("Here")
                if(self.maze2DArray[row][column] == "*"):
                    self.goals.append([row,column])
        #print("Goals:", self.goals)
        self.mazeNodes = {}
        #print("len", len(self.mazeNodes[0]))
        ## Make an equivalent way to store the nodes, then we will start checking adjacency
        testNode = Node(2,1,self)
        #print("testNode")
        #testNode.printXY()

        for row in range(self.mazeRows):
            #print("Loop row", row)
            for column in range(self.mazeColumns):
                #print("row", self.mazeNodes[row])
                self.mazeNodes[row, column] = Node(row,column,self)
                if(self.mazeNodes[row,column].isStart):
                    self.startNode = self.mazeNodes[row,column]
                #print("mazeNods test", self.mazeNodes[row,column].printXY())
        #print("mazeNods test", self.mazeNodes[2,1].printXY())
        #for child in self.mazeNodes[2,1].getChildren():
            #child.printXY()


    def printIndexes(self,listOfNodes):
        for i in range(len(listOfNodes)):
            print("Move", i, ". row: ",listOfNodes[i].row, ", column:",listOfNodes[i].column) 

    def reconstructPath(self,cameFrom, current): # Came from is a dictionary?
        total_path = [current]
        while current in cameFrom:
            current = cameFrom[current]
            total_path.insert(0,current)
        """ for i in range(len(total_path)):
            print("Move", i, ". row: ", total_path[i].row, ", column:",total_path[i].column) """
        #printIndexes(total_path)
        return total_path
# How aStar should work:
# Get the start node. Open a frontier that includes its children.
# Open the children and grab one that is lowest f(n) and 
    def aStar(self):
        cameFrom ={}
        print("Beginning aStar")
        node = self.startNode
        node.setPathCost(0) ##The start node has a path cost of zero.
        if (node.isGoal):
            return node
        frontier = []
        newQueue = minPriorityQueue()
        newQueue.insert(node)
        picked = []
        #picked.append([node.row,node.column])
        gns= {}
        gns[node] = 0
        #frontier.append(node)
        visited = {}
        visited[node] = True
        while (newQueue):
            currentNode = newQueue.delete()
            picked.append([currentNode.row,currentNode.column])
            print("CurrentNode:")
            currentNode.printXY()
            for child in currentNode.getChildren():
                currentDist = child.pathCost
                if(child.isGoal):
                    print("Reached childNode:", end ="")
                    child.printXY()
                    print("path cost:", child.getHeuristic())
                    picked.append([child.row, child.column])
                    return child, picked
                elif(child not in visited):
                    newQueue.insert(child)
                    visited[child] = True
            #print("frontier 0 ",frontier[0])
        for node in visited:
            print("Visited")
            node.printXY()

# Working version. Finds the optimal path and returns it as a list of nodes
    def aStarV2(self):
        cameFrom ={}
        #print("Beginning aStar")
        node = self.startNode
        node.setPathCost(0) ##The start node has a path cost of zero.
        if (node.isGoal):
            return node
        frontier = []
        newQueue = minPriorityQueue()
        newQueue.insert(node)
        #picked.append([node.row,node.column])
        gns= {}
        gns[node] = 0
        #frontier.append(node)
        pathTakenList = []
        visited = {}
        visited[node] = True
        currentNode = None
        while (newQueue.isEmpty()==False):
            currentNode = newQueue.delete()
            if(currentNode.isGoal):
                for nodes in self.reconstructPath(cameFrom,currentNode):
                    pathTakenList.append([nodes.row, nodes.column])
                return pathTakenList
                
            for child in currentNode.getChildren():
                currentDist = child.pathCost
                if( child not in gns or currentDist < gns[child]):
                    cameFrom[child] = currentNode
                    gns[child] = child.pathCost
                    putIn = True
                    for i in range(len(newQueue.queue)):
                        if(newQueue.queue[i]==child):
                            putIn = False
                    if(putIn): newQueue.insert(child)
        for nodes in self.reconstructPath(cameFrom,currentNode):
            pathTakenList.append([nodes.row, nodes.column])
        return pathTakenList
                    
    def dfsHelper(self, node, visited, check):
        visited[node] = [node.row, node.column]
        node.printXY()
        if(node.isGoal):
            print("\nFound goal.")
            check = 1
            return visited
        else:
            for child in node.getChildren():
                if (child not in visited) and (check ==0):
                    self.dfsHelper(child,visited, check)

    def DFS(self):
        print("Beginning DFS")
        node = self.startNode
        visited = {}
        return self.dfsHelper(node, visited, 0)

    def newDFS(self):
        print("start DFS: ")
        node = self.startNode
        print("From:", self.startNode.row, ",", self.startNode.column, "to")
        frontier =[node]
        visited = [node]
        bTPath = {}
        while len(frontier) > 0:
            currentNode = frontier.pop()
            if currentNode.isGoal:
                currentNode.printXY()
                print("Got it!")
                break
            for leaf in currentNode.getChildren():
                if leaf in visited:
                    continue
                visited.append(leaf)
                frontier.append(leaf)
                bTPath[leaf] = currentNode
        dfsPath = []
        dfsPath.append([self.startNode.row, self.startNode.column])
        for i in bTPath:
            dfsPath.append([i.row, i.column])
        return dfsPath

    def newBFS(self):
        print("start BFS: ")
        node = self.startNode
        print("From:", self.startNode.row, ",", self.startNode.column, "to")
        frontier =[node]
        visited = [node]
        bTPath = {}
        while len(frontier) > 0:
            currentNode = frontier.pop(0)
            if currentNode.isGoal:
                currentNode.printXY()
                print("Got it!")
                break
            for leaf in currentNode.getChildren():
                if leaf in visited:
                    continue
                visited.append(leaf)
                frontier.append(leaf)
                bTPath[leaf] = currentNode
        bfsPath = []
        bfsPath.append([self.startNode.row, self.startNode.column])
        for i in bTPath:
            bfsPath.append([i.row, i.column])
        return bfsPath

    def BFS(self):
        print("Beginning BFS")

        node = self.startNode
        node.printXY()
        if(node.isGoal):
            return node
        frontier = []
        frontier.append(node)
        visited = {}
        visited[node] = True
        pathCoordinatesList = []
        #pathCoordinatesList.append([node.row, node.column])
        goalFound = False

        while (frontier):
            currentNode = frontier.pop(0)
            pathCoordinatesList.append([currentNode.row, currentNode.column])
            print("CurrentNode: ", end = "")
            currentNode.printXY()
            for child in currentNode.getChildren():
                if(child.isGoal):
                    pathCoordinatesList.append([child.row, child.column])
                    return pathCoordinatesList
                elif child not in visited:
                    visited[child]=True
                    frontier.append(child)
            #print("frontier 0 ",frontier[0])
        #for node in visited:
            #print("Visited")
        
        return "Failed"
        

    def mazeToString(self):
        #print("Printing maze")
        for i in range(self.mazeRows):
            print(self.maze2DArray[i], end ="")
        print()
    def spaceToString(self, row, column):
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


mazeFile = "maze-2.txt"
maze = mazeReader(mazeFile)


newbfs = maze.newBFS()
print(newbfs)

dfsPath = maze.newDFS()
print(dfsPath)

aStarPath = maze.aStarV2()
print(aStarPath)
print("aStar Moves: " , len(aStarPath))